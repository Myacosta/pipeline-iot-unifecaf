import os
import pandas as pd
from sqlalchemy import create_engine, text


# ==========================================
# LOCALIZA A PASTA DO PROJETO
# ==========================================

pasta_projeto = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

pasta_data = os.path.join(
    pasta_projeto,
    "data"
)


# ==========================================
# LOCALIZA O CSV
# ==========================================

arquivos_csv = [
    arquivo
    for arquivo in os.listdir(pasta_data)
    if arquivo.lower().endswith(".csv")
]

if not arquivos_csv:
    raise FileNotFoundError(
        "Nenhum arquivo CSV encontrado na pasta data."
    )

nome_csv = arquivos_csv[0]

caminho_csv = os.path.join(
    pasta_data,
    nome_csv
)


# ==========================================
# LÊ O CSV
# ==========================================

print("Lendo o arquivo CSV...")

df = pd.read_csv(caminho_csv)

print("CSV lido com sucesso!")
print("Quantidade de registros:", len(df))

print("\nPrimeiros registros:")
print(df.head())


# ==========================================
# CONEXÃO COM POSTGRESQL
# ==========================================

usuario = "postgres"
senha = "postgres"
host = "localhost"
porta = "5432"
banco = "pipeline"


url = (
    f"postgresql+psycopg2://"
    f"{usuario}:{senha}@{host}:{porta}/{banco}"
)


print("\nConectando ao PostgreSQL...")

try:

    engine = create_engine(url)

    with engine.connect() as conexao:
        conexao.execute(text("SELECT 1"))

    print("Conexão com PostgreSQL realizada com sucesso!")

except Exception as erro:

    print("ERRO ao conectar ao PostgreSQL:")
    print(erro)

    raise SystemExit


# ==========================================
# ENVIA OS DADOS PARA O POSTGRESQL
# ==========================================

print("\nEnviando dados para o PostgreSQL...")

try:

    df.to_sql(
        "temperature_readings",
        engine,
        if_exists="replace",
        index=False
    )

    print("Dados enviados com sucesso!")

except Exception as erro:

    print("ERRO ao enviar os dados:")
    print(erro)

    raise SystemExit


# ==========================================
# CONFIRMA A QUANTIDADE DE REGISTROS
# ==========================================

try:

    with engine.connect() as conexao:

        resultado = conexao.execute(
            text(
                "SELECT COUNT(*) "
                "FROM temperature_readings"
            )
        )

        quantidade = resultado.scalar()

    print("\n================================")
    print("PROCESSAMENTO CONCLUÍDO")
    print("================================")
    print(
        "Registros no PostgreSQL:",
        quantidade
    )

except Exception as erro:

    print("ERRO ao consultar a tabela:")
    print(erro)