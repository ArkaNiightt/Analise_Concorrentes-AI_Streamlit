<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>ANALISE_CONCORRENTES-AI_STREAMLIT</h1>
<p align="left">
	<em>Desbloqueando o poder da IA para Análise Competitiva no Instagram!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/ArkaNiightt/Analise_Concorrentes-AI_Streamlit?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ArkaNiightt/Analise_Concorrentes-AI_Streamlit?style=for-the-badge&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ArkaNiightt/Analise_Concorrentes-AI_Streamlit?style=for-the-badge&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ArkaNiightt/Analise_Concorrentes-AI_Streamlit?style=for-the-badge&color=0080ff" alt="repo-language-count">
</p>
<p align="left">Construído com as ferramentas e tecnologias:</p>
<p align="left">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
</p>
</div>
<br clear="right">

## 🔗 Índice

- [📍 Visão Geral](#-visao-geral)
- [🦾 Funcionalidades](#-funcionalidades)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
  - [📂 Índice do Projeto](#-indice-do-projeto)
- [🚀 Começando](#-comecando)
  - [☑️ Requisitos](#-requisitos)
  - [⚙️ Instalação](#-instalacao)
  - [🤖 Uso](#-uso)
  - [🧪 Testes](#-testes)
- [📌 Roteiro do Projeto](#-roteiro-do-projeto)
- [🔰 Contribuição](#-contribuicao)
- [🎗 Licença](#-licenca)
- [🤜 Agradecimentos](#-agradecimentos)

---

## 📍 Visão Geral

O projeto AnaliseConcorrentes-AIStreamlit é uma ferramenta poderosa para profissionais de marketing no Instagram, oferecendo insights profundos sobre desempenho de conteúdo e análise de concorrentes. Utilizando IA, ele identifica padrões de engajamento, sugere os melhores horários para postagem e fornece estratégias de marketing. Seus painéis interativos e relatórios para download tornam a análise de dados intuitiva. Este projeto é um divisor de águas para quem busca otimizar sua estratégia no Instagram.

---

## 🦾 Funcionalidades

|      | Funcionalidade  | Resumo       |
| :--- | :---:           | :---          |
| ⚙️  | **Arquitetura**  | <ul><li>O projeto é estruturado em scripts Python, principalmente localizados no diretório `dashbords`.</li><li>Utiliza uma arquitetura modular com scripts separados para diferentes funcionalidades, como `analise_top_20.py`, `app.py`, `analise_with_gpt.py` e `analise_dados_estatisticas_gerais.py`.</li><li>O script `data_conection.py` lida com as conexões e a recuperação de dados do banco de dados.</li></ul> |
| 🔩 | **Qualidade do Código**  | <ul><li>O código é escrito em Python, seguindo as convenções padrão de codificação em Python.</li><li>Utiliza bibliotecas Python para várias funcionalidades, garantindo um código eficiente e limpo.</li><li>O tratamento de exceções é implementado em scripts como `analise_with_gpt.py` para garantir uma operação tranquila.</li></ul> |
| 📄 | **Documentação** | <ul><li>O idioma principal do projeto é Python, com um total de 5 arquivos Python e 1 arquivo de texto.</li><li>Comandos de instalação e uso são fornecidos na documentação, facilitando a configuração e o uso.</li><li>As dependências são claramente listadas no arquivo `requirements.txt`.</li></ul> |
| 🔌 | **Integrações**  | <ul><li>O projeto integra-se com o banco de dados Supabase para recuperação e manipulação de dados.</li><li>Utiliza o modelo OpenAI GPT para análise de dados baseada em IA.</li><li>Streamlit é usado para visualização de dados e criação de painéis interativos.</li></ul> |
| 🥩 | **Modularidade**    | <ul><li>O projeto é altamente modular com scripts separados para diferentes funcionalidades.</li><li>Código relacionado à conexão e recuperação de dados do banco de dados está encapsulado no script `data_conection.py`.</li><li>A análise baseada em IA e a visualização de dados são tratadas por scripts separados, promovendo a reutilização e a manutenção do código.</li></ul> |
| 🧪 | **Testes**       | <ul><li>Os comandos de teste são fornecidos na documentação, sugerindo o uso de `pytest` para testes.</li><li>No entanto, casos de teste específicos ou arquivos de teste não são visíveis nos detalhes fornecidos.</li></ul> |
| ⚡️  | **Desempenho**   | <ul><li>O projeto utiliza Python, uma linguagem de programação de alto nível conhecida por seu desempenho eficiente.</li><li>Utiliza bibliotecas Python eficientes como pandas para manipulação de dados, garantindo desempenho ótimo.</li></ul> |
| 🚡 | **Segurança**      | <ul><li>Aspectos de segurança não são explicitamente mencionados nos detalhes fornecidos.</li><li>No entanto, o uso de `python-dotenv` sugere que dados sensíveis, como credenciais do banco de dados, provavelmente são armazenados em um arquivo `.env`, promovendo boas práticas de segurança.</li></ul> |

---

## 📁 Estrutura do Projeto

```sh
└── Analise_Concorrentes-AI_Streamlit/
    ├── LICENSE
    ├── README.md
    ├── dashbords
    │   ├── __init__.py
    │   ├── analise_dados_estatisticas_gerais.py
    │   ├── analise_top_20.py
    │   ├── analise_with_gpt.py
    │   ├── app.py
    │   └── database
    │       ├── __init__.py
    │       └── data_conection.py
    └── requirements.txt
```


### 📂 Índice do Projeto
<details open>
	<summary><b><code>ANALISE_CONCORRENTES-AI_STREAMLIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- O arquivo Requirements.txt serve como um manifesto para as dependências do projeto, especificando as bibliotecas Python necessárias para o funcionamento adequado da aplicação<br>- Inclui bibliotecas para operações de IA (openai), gestão de ambiente (python-dotenv), manipulação de dados (pandas), visualização de dados (streamlit, plotly-express), operações de banco de dados (supabase) e manipulação de arquivos Excel (XlsxWriter).</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- dashbords Submodule -->
		<summary><b>dashbords</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/master/dashbords/analise_top_20.py'>analise_top_20.py</a></b></td>
				<td>- O script 'analise_top_20.py' realiza uma análise detalhada do desempenho de conteúdo no Instagram<br>- Gera insights sobre as principais postagens, engajamento dos usuários e desempenho do tipo de conteúdo<br>- O script também utiliza inteligência artificial (GPT) para fornecer insights de marketing<br>- Os resultados são exibidos em vários formatos, incluindo gráficos de barras, data frames e arquivos Excel e JSON para download.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/master/dashbords/app.py'>app.py</a></b></td>
				<td>- App.py serve como o ponto de entrada principal para a aplicação de painéis, permitindo que os usuários selecionem entre as opções "Análise Geral" e "Top 20"<br>- Ele integra funcionalidades dos módulos 'analise_dados_estatisticas_gerais' e 'analise_top_20', fornecendo uma interface amigável para análise de dados e insights sobre concorrentes.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/master/dashbords/analise_with_gpt.py'>analise_with_gpt.py</a></b></td>
				<td>- O script 'analise_with_gpt.py' no diretório 'dashboards' utiliza o modelo OpenAI GPT para analisar dados do Instagram, fornecendo insights de marketing<br>- Gera análises comparativas, identifica padrões de engajamento, sugere os melhores horários para postar e categoriza o conteúdo semanticamente<br>- O script também lida com exceções, garantindo uma operação tranquila.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/master/dashbords/analise_dados_estatisticas_gerais.py'>analise_dados_estatisticas_gerais.py</a></b></td>
				<td>- O arquivo 'analise_dados_estatisticas_gerais.py' no diretório 'dashboards' é uma aplicação de painéis que visualiza e analisa dados de usuários de um banco de dados<br>- Fornece análise de dados interativa, gera insights estatísticos e oferece sugestões de marketing baseadas em modelos de IA<br>- O painel também permite que os usuários filtrem os dados pelo nome de usuário e baixem os dados analisados como um arquivo Excel.</td>
			</tr>
			</table>
			<details>
				<summary><b>database</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/master/dashbords/database/data_conection.py'>data_conection.py</a></b></td>
						<td>- DataConnection em dashbords/database/data_conection.py estabelece uma conexão com o banco de dados Supabase, recupera e processa dados para vários casos de uso<br>- Recupera todos os dados, dados específicos com base no nome do proprietário, 20 principais registros e dados completos, incluindo URL<br>- Esses dados são essenciais para a funcionalidade do painel e interação do usuário.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Começando

### ☑️ Requisitos

Antes de começar com o Analise_Concorrentes-AI_Streamlit, certifique-se de que seu ambiente de execução atenda aos seguintes requisitos:

- **Linguagem de Programação:** Python
- **Gerenciador de Pacotes:** Pip


### ⚙️ Instalação

Instale o Analise_Concorrentes-AI_Streamlit usando um dos seguintes métodos:

**Construir a partir do código-fonte:**

1. Clone o repositório Analise_Concorrentes-AI_Streamlit:
```sh
❟ git clone https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit
```

2. Navegue até o diretório do projeto:
```sh
❟ cd Analise_Concorrentes-AI_Streamlit
```

3. Instale as dependências do projeto:


**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❟ pip install -r requirements.txt
```




### 🤖 Uso
Execute o Analise_Concorrentes-AI_Streamlit usando o seguinte comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❟ python {entrypoint}
```


### 🧪 Testes
Execute a suite de testes usando o seguinte comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❟ pytest
```


---
## 📌 Roteiro do Projeto

- [X] **`Tarefa 1`**: <strike>Implementar a funcionalidade um.</strike>
- [ ] **`Tarefa 2`**: Implementar a funcionalidade dois.
- [ ] **`Tarefa 3`**: Implementar a funcionalidade três.

---

## 🔰 Contribuição

- **💬 [Participe das Discussões](https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/discussions)**: Compartilhe suas ideias, forneça feedback ou faça perguntas.
- **🐛 [Reporte Problemas](https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/issues)**: Envie bugs encontrados ou registre solicitações de funcionalidades para o projeto `Analise_Concorrentes-AI_Streamlit`.
- **💡 [Envie Pull Requests](https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/blob/main/CONTRIBUTING.md)**: Revise PRs abertos e envie seus próprios PRs.

<details closed>
<summary>Diretrizes de Contribuição</summary>

1. **Faça um Fork do Repositório**: Comece fazendo um fork do repositório do projeto na sua conta do github.
2. **Clone Localmente**: Clone o repositório forkado para sua máquina local usando um cliente git.
   ```sh
   git clone https://github.com/ArkaNiightt/Analise_Concorrentes-AI_Streamlit
   ```
3. **Crie um Novo Branch**: Sempre trabalhe em um novo branch, dando um nome descritivo a ele.
   ```sh
   git checkout -b nova-funcionalidade-x
   ```
4. **Faça suas Mudanças**: Desenvolva e teste suas mudanças localmente.
5. **Commit suas Mudanças**: Faça o commit com uma mensagem clara descrevendo suas atualizações.
   ```sh
   git commit -m 'Implementada nova funcionalidade x.'
   ```
6. **Push para o GitHub**: Envie as mudanças para o repositório forkado.
   ```sh
   git push origin nova-funcionalidade-x
   ```
7. **Envie um Pull Request**: Crie um PR contra o repositório original. Descreva claramente as mudanças e suas motivações.
8. **Revisão**: Assim que seu PR for revisado e aprovado, ele será mesclado ao branch principal. Parabéns pela sua contribuição!
</details>

<details open>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com{/ArkaNiightt/Analise_Concorrentes-AI_Streamlit/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ArkaNiightt/Analise_Concorrentes-AI_Streamlit">
   </a>
</p>
</details>

---
