# Streamlit Instagram Dashboard

## Descrição

Este projeto é um dashboard interativo desenvolvido com Streamlit para analisar dados de concorrentes no Instagram. Ele permite visualizar métricas importantes, comparar desempenho entre diferentes usuários e obter insights de marketing gerados por uma inteligência artificial (GPT).

## Funcionalidades

- **Análise Geral**: Visualize estatísticas gerais, distribuição de tipos de postagens, análise de vídeos, relação entre likes e comentários, e obtenha insights de marketing.
- **Top 20**: Veja os 20 conteúdos mais populares de cada plataforma com base em diferentes métricas (likes, comentários, visualizações de vídeo, reproduções de vídeo).

## Estrutura do Projeto

- `app.py`: Arquivo principal que configura e executa o dashboard.
- `analise_dados_estatisticas_gerais.py`: Contém a lógica para renderizar a análise geral dos dados.
- `analise_top_20.py`: Contém a lógica para renderizar o top 20 conteúdos populares.
- `data_conection.py`: Gerencia a conexão com o banco de dados Supabase e a obtenção dos dados.
- `analise_with_gpt.py`: Integração com a API do OpenAI para gerar insights de marketing.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Streamlit_Instagram
    ```
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Configure as variáveis de ambiente no arquivo `.streamlit/secrets.toml`:
    ```
    SUPABASE_URL="<sua_supabase_url>"
    SUPABASE_KEY="<sua_supabase_key>"
    SUPABASE_DB="<seu_supabase_db>"
    OPENAI_API_KEY="<sua_openai_api_key>"
    ```

## Uso

1. Execute o aplicativo Streamlit:
    ```bash
    streamlit run app.py
    ```
2. Acesse o dashboard no seu navegador em `http://localhost:8501`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [MIT](LICENSE) para mais detalhes.