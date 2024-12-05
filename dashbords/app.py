import streamlit as st
from dashboard_streamlit_postgres import Dashboard
from analise_top_20 import render_dashboard

st.set_page_config(page_title="Análise de Dados de Concorrentes", page_icon="📈",layout="wide")

dashboard = Dashboard()



def analise_dashbord_():
    st.header("📥 Analise AI")
    st.write("### Faça uma analise definitiva de diferentes plataformas.")
    st.markdown("---")


def highlights_top_20():
    st.header("📥 Ver Top 20 de Cada Plataforma")
    st.write("### Visualize top 20 posts de cada plataforma")
    st.markdown("---")


# Função principal do aplicativo
def main():
    # Configuração da página deve ser a primeira chamada
    st.title("🤖 Ferramentas Marketing")
    st.sidebar.title("⚙️ Escolha a ferramenta")
    st.sidebar.markdown("Selecione uma das opções abaixo para começar:")
    opcao = st.sidebar.radio("Selecione uma opção:", ["Analise Geral", "Top 20"])

    st.markdown("---")
    if opcao == "Analise Geral":
        dashboard.render()
    elif opcao == "Top 20":
        render_dashboard()

    st.sidebar.markdown("---")
    st.sidebar.info(
        "Dica: Certifique-se de usar a melhor ferramenta para obter os melhores resultados."
    )


if __name__ == "__main__":
    main()
