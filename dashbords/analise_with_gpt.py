from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from supabase import create_client, Client
import streamlit as st

load_dotenv()

# Configuração do Supabase
supabase_url = st.secrets["SUPABASE_URL"]
supabase_key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(supabase_url, supabase_key)

DATABASE = st.secrets["SUPABASE_DB"]


def get_data_from_supabase(ownerusername):
    try:
        response = (
            supabase.table(f"{DATABASE}")
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

        data = response.data
        if data:
            columns = list(data[0].keys())
            rows = [list(item.values()) for item in data]
            return columns, rows
        else:
            return [], []

    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return [], []


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def analyze_data_with_gpt(columns, data, model="gpt-4o", temperature=0.5):
    if not columns or not data:
        return "Não foi possível obter os dados para análise."

    df = pd.DataFrame(data, columns=columns)
    data_str = df.to_string(index=False)

    prompt = f"""Analise os seguintes dados do Instagram e forneça insights de marketing:

    Colunas: {', '.join(columns)}

    Dados:
    {data_str}

    Com base nesses dados, forneça uma análise comparativa dos resultados das empresas, observando o engajamento e oferecendo recomendações de marketing:
    1. Comparação entre as diferentes empresas em termos de engajamento (comentários e curtidas).
    2. Tipos de conteúdo que têm melhor desempenho para cada empresa.
    3. Padrões de engajamento que se destacam.
    4. Melhores horários para postagem para maximizar o engajamento.
    5. Usuários mais influentes em cada empresa.
    6. Desempenho de vídeos em comparação a outros tipos de conteúdo.
    7. Temas ou tópicos que geram mais engajamento.
    8. Recomendações específicas para melhorar o engajamento de cada empresa.
    9. Segmente semanticamente pelo significado das palavras, categorizando cada parte dos elementos 'captions' enviada em {data_str}, com isso crie categorias [
    "Recursos e ferramentas",
    "Motivacional",
    "Eventos e Promoções",
    "Histórias de sucesso",
    "Educacional",
    "Dicas e conselhos",
    "Humor/Descontração", Crie mais 10 categorias...] que mais aparecem, mostrando quantas vezes aparece.

    Por favor, forneça uma análise detalhada e acionável para cada ponto. Vale entender que alguns valores vão estar com valor -1, isso quer dizer que foi desabilitada, por exemplo: 'likescount=-1 quer dizer que os comentários foram desabilitados.'
    """

    try:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um analista de marketing especializado em dados do Instagram.",
                },
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Erro ao chamar a API do OpenAI: {e}")
        return "Erro ao obter resposta do GPT para este conjunto de dados."
