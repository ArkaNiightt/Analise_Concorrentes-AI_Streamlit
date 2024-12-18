import streamlit as st

st.set_page_config(page_title="Análise de Dados de Concorrentes", page_icon="📈", layout="wide")


from analise_dados_estatisticas_gerais import Dashboard
import analise_top_20

dashboard_analise_estatisticas_gerais = Dashboard()

# Função principal do aplicativo
def main():
    # Configuração da página deve ser a primeira chamada
    st.title("🤖 Ferramentas Marketing")
    
    # Sidebar styling and options
    with st.sidebar:
        st.title("⚙️ Escolha a ferramenta")
        st.markdown("Selecione uma das opções abaixo para começar:")
        
        opcao = st.selectbox(
            "Escolha sua análise:",
            ["Analise Geral", "Top 20"],
            format_func=lambda x: f"📊 {x}",
            help="Selecione o tipo de análise que deseja realizar"
        )
        
    st.markdown("---")
    if opcao == "Analise Geral":
        dashboard_analise_estatisticas_gerais.render()
        st.toast("Dados carregados com sucesso.", icon="✅")
    elif opcao == "Top 20":
        analise_top_20.render()
        st.toast("Dados carregados com sucesso.", icon="✅")

    st.sidebar.markdown("---")
    with st.sidebar:
        st.info(
            "💡 Dica: Certifique-se de usar a melhor ferramenta para obter os melhores resultados."
        )


if __name__ == "__main__":
    main()
