import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import pandas as pd
import logging

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

DATABASE = os.getenv("SUPABASE_DB")

class DatabaseConnection:
    @staticmethod
    @st.cache_data
    def get_data():
        try:
            response = supabase.table(DATABASE).select("*").execute()
            
            if response.data:
                df = pd.DataFrame(response.data)
                return df
            else:
                logging.error("Erro ao obter dados do Supabase: Nenhum dado retornado.")
                st.error("Erro ao obter dados do banco de dados: Nenhum dado retornado.")
                return pd.DataFrame()
        except Exception as e:
            logging.error(f"Erro ao conectar ao banco de dados: {e}")
            st.error(f"Erro ao conectar ao banco de dados: {e}")
            return pd.DataFrame()

def filter_top_20_per_owner(data, filter_option):
    top_20_per_owner = []
    for owner, group in data.groupby("ownerusername"):
        top_20 = group.sort_values(by=filter_option, ascending=False).head(20)
        top_20_per_owner.append((owner, top_20))
    return top_20_per_owner

def render_dashboard():
    st.title("📊 Top 20 Conteúdos Populares")
    st.markdown(
        """
        ### Bem-vindo ao Painel de Top 20 Conteúdos!
        Nesta aplicação, você pode visualizar os conteúdos mais populares (vídeos, sidecars, imagens) com base em diferentes métricas.
        """
    )
    st.markdown("---")

    with st.spinner("Carregando dados..."):
        df = DatabaseConnection.get_data()

    if df.empty:
        st.warning("Nenhum dado encontrado.")
        return

    filter_option = st.selectbox(
        "Selecione o critério para o Top 20:",
        ("likescount", "commentscount", "videoviewcount", "videoplaycount")
    )

    top_20_per_owner = filter_top_20_per_owner(df, filter_option)

    for owner, top_20_df in top_20_per_owner:
        st.subheader(f"🔝 Top 20 conteúdos para **{owner}** baseado em **{filter_option}**")
        st.markdown("Veja abaixo os conteúdos mais populares de acordo com a métrica selecionada:")
        st.dataframe(top_20_df, use_container_width=True)

    
    total_values = df.groupby("ownerusername")[filter_option].sum().reset_index()

    st.markdown("### 📊 Comparação dos Ownerusernames")
    st.bar_chart(total_values.set_index("ownerusername")[filter_option])

if __name__ == "__main__":
    render_dashboard()
