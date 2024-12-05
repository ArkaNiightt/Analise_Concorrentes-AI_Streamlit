import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from analise_with_gpt import analyze_data_with_gpt
import logging
from io import BytesIO
from database import data_conection

data_conection = data_conection.DatabaseConnection

# Configuração do logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Carregar variáveis de ambiente
load_dotenv()

class Dashboard:
    def __init__(self):
        self.data = data_conection.get_all_data()
        self.data_filtered = None
        self.selected_username = None

    def render_sidebar(self):
        st.header("Filtros")
        if not self.data.empty:
            self.selected_username = st.selectbox(
                "Selecione o dono do post: ",
                options=self.data["ownerusername"].unique(),
            )
            self.data_filtered = self.data[
                self.data["ownerusername"] == self.selected_username
            ]
            if st.button("Atualizar Dados"):
                st.cache_data.clear()
                self.data = data_conection.get_all_data()
        else:
            st.write("Nenhum dado disponível para filtrar.")

    def render_overview(self):
        if self.selected_username:
            st.title(
                f"📈 Análise Interativa dos Dados do Usuário: {self.selected_username}"
            )
            st.markdown(
                "Explore as métricas e dados de postagens, visualizando insights importantes de forma interativa e atraente."
            )

    def render_post_type_distribution(self):
        if self.data_filtered is not None and not self.data_filtered.empty:
            post_type_counts = self.data_filtered["type"].value_counts()
            fig = px.pie(
                names=post_type_counts.index,
                values=post_type_counts,
                title="Distribuição dos Tipos de Postagens",
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.RdBu,
            )
            st.plotly_chart(fig)

    def render_general_statistics(self):
        if self.data_filtered is not None and not self.data_filtered.empty:
            st.subheader("📈 Estatísticas Gerais")
            if (
                "commentscount" in self.data_filtered.columns
                and "likescount" in self.data_filtered.columns
            ):
                avg_comments = self.data_filtered["commentscount"].clip(lower=0).mean()
                avg_likes = self.data_filtered["likescount"].clip(lower=0).mean()
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(
                        label="Média de Comentários",
                        value=f"{avg_comments:,.2f}".replace(",", "."),
                    )
                with col2:
                    st.metric(
                        label="Média de Likes",
                        value=f"{avg_likes:,.2f}".replace(",", "."),
                    )

    def render_video_analysis(self):
        if self.data_filtered is not None and not self.data_filtered.empty:
            # Filtrando apenas os dados do tipo "Video"
            video_data = self.data_filtered[self.data_filtered["type"] == "Video"]
            video_data_frame = video_data[
                [
                    "videoplaycount",
                    "videoviewcount",
                    "likescount",
                    "commentscount",
                    "url",
                    "ownerusername",
                    "type",
                ]
            ]
            if not video_data.empty:
                st.subheader("🎥 Análise de Vídeos")

                # Cálculo das médias de visualizações e reproduções de vídeos
                video_view_mean = video_data["videoviewcount"].mean()
                video_play_mean = video_data["videoplaycount"].mean()

                # Exibição das métricas de média de visualizações e reproduções
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(
                        label="Média de Visualizações de Vídeos",
                        value=f"{video_view_mean:,.2f}".replace(",", "."),
                    )
                with col2:
                    st.metric(
                        label="Média de Reproduções de Vídeos",
                        value=f"{video_play_mean:,.2f}".replace(",", "."),
                    )

                # Comparativo entre visualizações e reproduções de vídeos
                fig = px.scatter(
                    video_data,
                    x="videoplaycount",
                    y="videoviewcount",
                    hover_data=["url"],
                    custom_data=["url"],
                    title="Relação entre Reproduções e Visualizações de Vídeos",
                    labels={
                        "videoplaycount": "Reproduções de Vídeos",
                        "videoviewcount": "Visualizações de Vídeos",
                        "url": "URL do Vídeo",
                    },
                    color_discrete_sequence=["#636EFA"],
                    template="plotly_white",
                )
                st.plotly_chart(fig, use_container_width=True)

                # Visualização do DataFrame
                st.subheader("📊 Dados Filtrados para Análise de Vídeos")
                st.dataframe(video_data_frame, use_container_width=True)

    def render_likes_comments_scatter(self):
        if self.data_filtered is not None and not self.data_filtered.empty:
            st.subheader("👍 Likes x Comentários 💬")
            filtered_data = self.data_filtered.copy()
            filtered_data_frame = filtered_data[
                ["likescount", "commentscount", "url", "type", "ownerusername"]
            ]
            filtered_data["likescount"] = filtered_data["likescount"].apply(
                lambda x: max(0, x)
            )
            filtered_data["commentscount"] = filtered_data["commentscount"].apply(
                lambda x: max(0, x)
            )
            fig = px.scatter(
                filtered_data,
                x="likescount",
                y="commentscount",
                title="Relacionamento entre Likes e Comentários",
                labels={"likescount": "Likes", "commentscount": "Comentários"},
                color_discrete_sequence=["#EF553B"],
                template="plotly_white",
            )
            st.plotly_chart(fig)

            # Visualização do DataFrame
            st.subheader("📊 Dados Filtrados para Likes x Comentários")
            st.dataframe(filtered_data_frame, use_container_width=True)

    def render_observations(self):
        if self.data_filtered is not None and not self.data_filtered.empty:
            show_insights = st.checkbox("Ver Insights de Marketing (GPT)")
            if show_insights:
                st.info(
                    "Os insights a seguir foram gerados por uma Inteligência Artificial (GPT) e devem ser utilizados como sugestões, podendo não ser 100% precisos."
                )
                # Integrando a análise do GPT
                columns, data = data_conection.get_data_from_supabase_for_gpt(self.selected_username)
                if columns and data:
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
                            insights = analyze_data_with_gpt(
                                columns, data, model=model, temperature=temperature
                            )
                        if insights:
                            st.write("## Insights de Marketing (GPT)")
                            st.markdown(insights)

    def convert_df_to_excel(self, df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Transações")
        output.seek(
            0
        )  # Certifique-se de voltar para o início do arquivo antes de retorná-lo
        return output.getvalue()

    def render_data_table(self):
        if self.data_filtered is not None and not self.data_filtered.empty:
            pagina = str(self.selected_username).upper()

            st.subheader(f"📋 Visualização Geral dos Dados da Página: {pagina}")
            st.dataframe(self.data_filtered)

            # Corrigido: passar o DataFrame corretamente
            st.download_button(
                label="💽 Baixar planilha como XLSX",
                data=self.convert_df_to_excel(self.data_filtered),
                file_name=f"concorrentes_({self.selected_username}).xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

    def render(self):
        self.render_sidebar()
        self.render_overview()
        self.render_post_type_distribution()
        self.render_general_statistics()
        self.render_video_analysis()
        self.render_likes_comments_scatter()
        self.render_data_table()
        self.render_observations()


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.render()
