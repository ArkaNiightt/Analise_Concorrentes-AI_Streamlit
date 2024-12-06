import streamlit as st
import pandas as pd
from io import BytesIO
from dotenv import load_dotenv
from database import data_conection
from analise_with_gpt import analyze_data_with_gpt_top_20
import json
import plotly.express as px

# Carregar variáveis de ambiente
load_dotenv()


df = data_conection.DatabaseConnection().get_data()


def filter_top_20_combined(data, filter_option):
    # Usando list comprehension ao invés de um loop for tradicional
    top_20_per_owner = [
        group.nlargest(20, columns=filter_option).assign(ownerusername=owner)
        for owner, group in data.groupby("ownerusername")
    ]

    # Verifica se a lista não está vazia antes de fazer a concatenação
    if not top_20_per_owner:
        return pd.DataFrame()

    # Concatena e ordena os resultados
    return (
        pd.concat(top_20_per_owner, ignore_index=True)
        .nlargest(n=len(data), columns=filter_option)
        .reset_index(drop=True)
    )


def filter_top_20_per_owner(data, filter_option):
    # Using list comprehension to create a dictionary structure
    result = {
        owner: group.nlargest(20, columns=filter_option)
        .reset_index(drop=True)
        .to_dict("records")
        for owner, group in data.groupby("ownerusername")
    }
    return result


def display_likes_statistics(
    dataframe,
    metricas,
    filtro,
):

    top_20_per_owner = []
    for owner, group in dataframe.groupby("ownerusername"):
        top_20 = group.sort_values(by=filtro, ascending=False).head(20)
        top_20_reset = top_20.reset_index(drop=True)
        top_20_per_owner.append((owner, top_20_reset))

    # Preparar os dados para o gráfico
    chart_data = (
        pd.concat([group for _, group in top_20_per_owner])[["ownerusername", filtro]]
        .groupby("ownerusername")
        .mean()
        .reset_index()
    )

    # Arredondar os valores de likescount
    chart_data[filtro] = chart_data[filtro].round(2)

    st.markdown(f"#### 🔍 Média por ({metricas[filtro]})")
    st.write("")
    # Exibir o gráfico de barras
    st.bar_chart(chart_data.set_index("ownerusername"))


def display_types_statistics(dataframe, filtro):
    if filtro in ["likescount", "commentscount"]:
        st.markdown("#### 📊 Desempenho por Tipo de Conteúdo")
        # Usar o filter_top_20_combined para obter os top 20 posts
        filtered_data = filter_top_20_combined(dataframe, filtro)

        # Exibir o gráfico com tipo e ownerusername, com valores arredondados
        grouped_by_owner = (
            filtered_data.groupby(["ownerusername", "type"])[filtro]
            .mean()
            .round(2)
            .unstack()
        )
        st.bar_chart(grouped_by_owner)
        
        st.markdown("### 📊 Comparação Geral Detalhada Quantidade de Tipos de Postagens")
        post_type_counts = (
            dataframe.groupby(["type", "ownerusername"]).size().reset_index(name="count")
        )
        fig = px.bar(
            post_type_counts,
            x="type",
            y="count",
            color="ownerusername",
            title="Comparação de Tipos de Postagens por Usuário",
            barmode="group",  # Agrupar barras por ownerusername
            labels={
                "count": "Quantidade",
                "type": "Tipo de Postagem",
                "ownerusername": "Usuário",
            },
        )
        st.plotly_chart(fig)

    else:
        pass


def display_top_20_posts(dataframe, metricas, choice):

    st.dataframe(
        dataframe,
        use_container_width=True,
        column_order=["ownerusername", "type", choice, "url"],
        column_config={
            "url": st.column_config.LinkColumn(
                "Link", help="Clique para abrir o post no Instagram"
            ),
            "ownerusername": st.column_config.TextColumn("Pagina"),
            "type": st.column_config.TextColumn("Tipo"),
            choice: st.column_config.NumberColumn(metricas[choice]),
        },
    )


def analise_gpt(data):
    show_insights = st.checkbox("Ver Insights de Marketing (GPT)")
    if show_insights:
        st.info(
            "Os insights a seguir foram gerados por uma Inteligência Artificial (GPT) e devem ser utilizados como sugestões, podendo não ser 100% precisos."
        )
        if not df.empty:
            model = st.selectbox(
                "Escolha o modelo GPT:",
                [
                    "gpt-4o-mini",
                    "gpt-3.5-turbo",
                    "gpt-4o",
                ],
            )
            temperature = st.slider(
                "Temperatura do Modelo:",
                min_value=0.0,
                max_value=2.0,
                value=0.5,
            )
            if st.button("Executar Análise de Marketing (GPT)"):
                with st.spinner("Analisando dados..."):
                    insights = analyze_data_with_gpt_top_20(
                        data, model=model, temperature=temperature
                    )
                if insights:
                    st.write("## Insights de Marketing (GPT)")
                    st.markdown(insights)


def expander_detalhado(data, data_gpt):
    with st.expander("🔝 Top 20 Detalhado", expanded=False):
        st.dataframe(
            data,
            use_container_width=True,
            column_order=[
                "ownerusername",
                "type",
                "likescount",
                "commentscount",
                "videoviewcount",
                "videoplaycount",
                "url",
            ],
            column_config={
                "url": st.column_config.LinkColumn(
                    "Link", help="Clique para abrir o post no Instagram"
                ),
                "ownerusername": st.column_config.TextColumn("Pagina"),
                "type": st.column_config.TextColumn("Tipo"),
                "likescount": st.column_config.NumberColumn("Likes"),
                "commentscount": st.column_config.NumberColumn("Comentários"),
                "videoviewcount": st.column_config.NumberColumn("Visualizações Vídeo"),
                "videoplaycount": st.column_config.NumberColumn("Reprodução de Vídeo"),
            },
        )
        st.json(data_gpt, expanded=False)

        # Create Excel file in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            data.to_excel(writer, index=False, sheet_name="Sheet1")
        output.seek(0)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="💽 Baixar planilha como XLSX",
                data=output.getvalue(),
                file_name="concorrentes_(Top_20_Detalhado).xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

        with col2:
            if data_gpt:  # Check if data_gpt is not empty
                json_str = json.dumps(data_gpt, indent=2, ensure_ascii=False)
                st.download_button(
                    label="📥 Baixar JSON",
                    data=json_str,
                    file_name="concorrentes_top_20.json",
                    mime="application/json",
                )


def render():
    # Criar um dicionário com rótulos mais amigáveis
    metricas = {
        "likescount": "Número de Curtidas",
        "commentscount": "Número de Comentários",
        "videoviewcount": "Visualizações do Vídeo",
        "videoplaycount": "Reproduções do Vídeo",
    }

    # Criar selectbox com layout melhorado
    st.subheader("📊 Selecione a Métrica de Análise")
    choice = st.selectbox(
        "Escolha qual métrica você deseja analisar:",
        options=list(metricas.keys()),
        format_func=lambda x: metricas[x],
        help="Selecione uma métrica para visualizar as estatísticas correspondentes",
    )
    # Título principal com emoji e formatação
    st.title("📱 Análise de Dados do Instagram")

    # Descrição com mais contexto e estilo
    st.markdown(
        """
    ### 🎯 Objetivo
    Esta ferramenta oferece uma análise detalhada do desempenho de conteúdo no Instagram,
    permitindo visualizar métricas importantes e identificar tendências.
    
    """
    )
    st.markdown("---")

    display_likes_statistics(df, metricas=metricas, filtro=choice)

    display_types_statistics(df, filtro=choice)

    # Seção de top posts com estilo
    st.markdown("---")
    st.subheader("🏆 Top 20 Posts com Maior Engajamento por Página")
    st.markdown(
        """
    Abaixo estão listados os posts mais relevantes de cada página, ordenados pela métrica selecionada.
    Clique nos links para visualizar os posts diretamente no Instagram.
    """
    )
    top_20 = filter_top_20_combined(df, filter_option=choice)
    data_gpt = filter_top_20_per_owner(df, filter_option=choice)

    display_top_20_posts(top_20, metricas=metricas, choice=choice)
    
    st.write("")

    expander_detalhado(top_20, data_gpt)

    st.markdown("---")

    analise_gpt(data_gpt)


if __name__ == "__main__":
    render()
