import streamlit as st
from dotenv import load_dotenv
from database import data_conection
import pandas as pd
import plotly.express as px
from analise_with_gpt import analyze_data_with_gpt_top_20

# Carregar variáveis de ambiente
load_dotenv()


# Classe para lidar com as operações de filtro
class ContentFilter:
    @staticmethod
    def filter_top_20_per_owner(data, filter_option):
        top_20_per_owner = []
        for owner, group in data.groupby("ownerusername"):
            top_20 = group.sort_values(by=filter_option, ascending=False).head(20)
            top_20_reset = top_20.reset_index(drop=True)
            top_20_per_owner.append((owner, top_20_reset))
        return top_20_per_owner

    @staticmethod
    def filter_top_20_combined(data, filter_option):
        top_20_per_owner = []
        for owner, group in data.groupby("ownerusername"):
            top_20 = group.sort_values(by=filter_option, ascending=False).head(20)
            top_20["owner"] = owner
            top_20_per_owner.append(top_20)
        if top_20_per_owner:
            combined_top_20 = pd.concat(top_20_per_owner, ignore_index=True)
        else:
            combined_top_20 = pd.DataFrame()
        return combined_top_20


# Classe para lidar com o dashboard Streamlit
class DashboardRenderer:
    def __init__(self):
        self.db_handler = data_conection.DatabaseConnection()
        self.content_filter = ContentFilter()

    def render_dashboard(self):
        st.title("📊 Top 20 Conteúdos Populares")
        st.markdown(
            """
            ### Bem-vindo ao Painel de Top 20 Conteúdos!
            Nesta aplicação, você pode visualizar os conteúdos mais populares (vídeos, sidecars, imagens) com base em diferentes métricas.
            """
        )
        st.markdown("---")

        with st.spinner("Carregando dados..."):
            df = self.db_handler.get_data()

        if df is None or df.empty:
            st.warning("Nenhum dado encontrado.")
            return

        filter_option = st.selectbox(
            "Selecione o critério para o Top 20:",
            ("likescount", "commentscount", "videoviewcount", "videoplaycount"),
        )

        # Renderização do Top 20 Geral de Cada Plataforma
        st.subheader("🔝 Top 20 Geral de Cada Plataforma")
        combined_top_20 = self.content_filter.filter_top_20_combined(df, filter_option)
        if not combined_top_20.empty:
            st.dataframe(combined_top_20, use_container_width=True)
        else:
            st.warning("Nenhum dado para o Top 20 Geral de Cada Plataforma.")

        # Renderização do Top 20 por Plataforma
        top_20_per_owner = self.content_filter.filter_top_20_per_owner(
            df, filter_option
        )
        
        st.markdown("---")

        # Gráfico de Comparação de Tipos de Postagens
        if not combined_top_20.empty:
            st.markdown("### 📊 Comparação de Tipos de Postagens")
            post_type_counts = (
                combined_top_20.groupby(["type", "ownerusername"])
                .size()
                .reset_index(name="count")
            )
            fig = px.bar(
                post_type_counts,
                x="type",
                y="count",
                color="ownerusername",
                title="Comparação de Tipos de Postagens por Usuário",
            )
            st.plotly_chart(fig)
            
            st.markdown("---")
            

            # Média de Visualizações por Usuário
            st.markdown("### 📊 Média de Visualizações por Usuário")
            avg_views_per_owner = (
                combined_top_20.groupby("ownerusername")["videoviewcount"]
                .mean()
                .reset_index()
            )
            fig_avg = px.bar(
                avg_views_per_owner,
                x="ownerusername",
                y="videoviewcount",
                title="Média de Visualizações por Usuário",
                labels={
                    "videoviewcount": "Média de Visualizações",
                    "ownerusername": "Usuário",
                },
            )
            st.plotly_chart(fig_avg)
        else:
            st.warning(
                "Nenhum dado disponível para o gráfico de comparação de tipos de postagens."
            )
            
        st.markdown("---")
        
        # Gráfico de Comparação de Likes por Usuário
        total_likes = df.groupby("ownerusername")["likescount"].sum().reset_index()
        if not total_likes.empty:
            st.markdown("### 📊 Comparação de Likes por Usuário")
            fig_likes = px.bar(
                total_likes,
                x="ownerusername",
                y="likescount",
                title="Total de Likes por Usuário",
                labels={"likescount": "Total de Likes", "ownerusername": "Usuário"},
            )
            st.plotly_chart(fig_likes)
        else:
            st.warning("Nenhum dado para o gráfico de comparação de likes por usuário.")
            
        st.markdown("---")
        
        with st.expander("🔝 Top 20 de Cada Plataforma", expanded=True):
            if top_20_per_owner:
                for owner, top_20_df in top_20_per_owner:
                    st.subheader(
                        f"({str(owner).upper()}) baseado em {filter_option.replace('likescount', 'Likes').replace('commentscount', 'Comentários').replace('videoviewcount', 'Visualizações Vídeo').replace('videoplaycount', 'Reprodução de Vídeo')}"
                    )
                    st.markdown(
                        "Veja abaixo os conteúdos mais populares de acordo com a métrica selecionada:"
                    )
                    st.dataframe(top_20_df, use_container_width=True)
            else:
                st.warning("Nenhum dado para o Top 20 de Cada Plataforma.")

        st.markdown("---")

        show_insights = st.checkbox("Ver Insights de Marketing (GPT)")
        if show_insights:
            st.info(
                "Os insights a seguir foram gerados por uma Inteligência Artificial (GPT) e devem ser utilizados como sugestões, podendo não ser 100% precisos."
            )
            data = combined_top_20
            if not data.empty:
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
                    insights = analyze_data_with_gpt_top_20(
                        data, model=model, temperature=temperature
                    )
                    if insights:
                        st.write("## Insights de Marketing (GPT)")
                        st.markdown(insights)

    def render(self):
        self.render_dashboard()


if __name__ == "__main__":
    dashboard = DashboardRenderer()
    dashboard.render()
