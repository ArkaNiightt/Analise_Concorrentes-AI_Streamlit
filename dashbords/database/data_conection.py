import streamlit as st
import pandas as pd
import plotly.express as px
from supabase import create_client, Client
from supabase.client import ClientOptions


# Configuração do Supabase
supabase_url = st.secrets["SUPABASE_URL"]
supabase_key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(
    supabase_url,
    supabase_key,
    options=ClientOptions(
        postgrest_client_timeout=20,
        storage_client_timeout=20,
        schema="public",
    ),
)
DATABASE = st.secrets["SUPABASE_DB"]


@st.cache_data
def get_all_data():
    try:
        response = supabase.table(DATABASE).select("*").execute()

        if response.data:
            df = pd.DataFrame(response.data)
            return df
        else:
            st.error(
                "Erro ao obter dados do banco de dados: Nenhum dado retornado.",
                icon="❌",
            )
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}", icon="❌")
        return pd.DataFrame()
    except KeyboardInterrupt:
        st.error("Finalizado pelo usuário.", icon="⚠️")
        return []


@st.cache_data
def get_data_from_supabase_for_gpt(ownerusername):
    try:
        response = (
            supabase.table(DATABASE)
            .select(
                "ownerusername",
                "type",
                "likescount",
                "commentscount",
                "videoviewcount",
                "videoplaycount",
                "hashtags",
                "mentions",
                "caption",
            )
            .eq("ownerusername", ownerusername)
            .execute()
        )

        if response.data:
            df = pd.DataFrame(response.data)
            return df
        else:
            st.error(
                "Erro ao obter dados do banco de dados: Nenhum dado retornado.",
                icon="❌",
            )
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}", icon="❌")
        return pd.DataFrame()
    except KeyboardInterrupt:
        st.error("Finalizado pelo usuário.", icon="⚠️")
        return []


@st.cache_data
def get_data_from_supabase_for_gpt_top_20():
    try:
        response = (
            supabase.table(DATABASE)
            .select(
                "ownerusername",
                "type",
                "likescount",
                "commentscount",
                "videoviewcount",
                "videoplaycount",
                "hashtags",
                "mentions",
                "caption",
            )
            .execute()
        )

        if response.data:
            df = pd.DataFrame(response.data)
            return df
        else:
            st.error(
                "Erro ao obter dados do banco de dados: Nenhum dado retornado.",
                icon="❌",
            )
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}", icon="❌")
        return pd.DataFrame()
    except KeyboardInterrupt:
        st.error("Finalizado pelo usuário.", icon="⚠️")
        return []


@st.cache_data
def get_data():
    try:
        response = (
            supabase.table(DATABASE)
            .select(
                "ownerusername",
                "type",
                "likescount",
                "commentscount",
                "videoviewcount",
                "videoplaycount",
                "hashtags",
                "mentions",
                "caption",
                "url",
            )
            .execute()
        )

        if response.data:
            df = pd.DataFrame(response.data)
            return df
        else:
            st.error(
                "Erro ao obter dados do banco de dados: Nenhum dado retornado.",
                icon="❌",
            )
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}", icon="❌")
        return pd.DataFrame()
    except KeyboardInterrupt:
        st.error("Finalizado pelo usuário.", icon="⚠️")
        return []
