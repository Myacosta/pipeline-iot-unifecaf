# Pipeline de Dados com IoT e Docker

## Descrição
Projeto que processa leituras de temperatura de dispositivos IoT, armazena no PostgreSQL e exibe em um dashboard Streamlit.

## Tecnologias
Python, PostgreSQL, Docker, Streamlit, Plotly, Pandas

## Como usar
1. Coloque o CSV na pasta data/
2. Execute: docker-compose up -d
3. Execute: pip install -r requirements.txt
4. Execute: python src/processar_dados.py
5. Execute: streamlit run src/dashboard.py
6.