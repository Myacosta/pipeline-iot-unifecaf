import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


# ==========================================
# CONFIGURAÇÃO
# ==========================================

st.set_page_config(
    page_title="Pipeline IoT",
    page_icon="🌡️",
    layout="wide"
)


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


# ==========================================
# TÍTULO
# ==========================================

st.title("🌡️ Dashboard IoT")
st.subheader("Leitura de Temperatura")


# ==========================================
# CARREGA DADOS DO POSTGRESQL
# ==========================================

try:

    engine = create_engine(url)

    df = pd.read_sql(
        "SELECT * FROM vw_temperature_readings",
        engine
    )

    st.success(
        "Dados carregados do PostgreSQL com sucesso!"
    )

except Exception as erro:

    st.error(
        "Não foi possível conectar ao PostgreSQL."
    )

    st.code(str(erro))

    st.stop()


# ==========================================
# INDICADORES
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de registros",
        len(df)
    )

with col2:
    st.metric(
        "Total de colunas",
        len(df.columns)
    )

with col3:
    st.metric(
        "Valores vazios",
        int(df.isna().sum().sum())
    )


# ==========================================
# TABELA
# ==========================================

st.subheader("📊 Dados de temperatura")

st.dataframe(
    df,
    use_container_width=True
)


# ==========================================
# ESTATÍSTICAS
# ==========================================

st.subheader("📈 Resumo das temperaturas")

st.dataframe(
    df.describe(),
    use_container_width=True
)


# ==========================================
# GRÁFICO
# ==========================================

st.subheader("🌡️ Temperaturas")

st.line_chart(
    df["temp"].head(500)
)


# ==========================================
# INFORMAÇÕES
# ==========================================

st.subheader("ℹ️ Informações do Pipeline")

st.write(
    "Fonte dos dados: PostgreSQL"
)

st.write(
    "Tabela: temperature_readings"
)

st.write(
    "View: vw_temperature_readings"
)

st.write(
    f"Total de registros carregados: **{len(df)}**"
)