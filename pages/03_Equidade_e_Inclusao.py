import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, filtro_df

st.set_page_config(page_title="Equidade & Inclusão • Painel Educacional PB", page_icon="⚖️", layout="wide")

df = load_data("data/indicadores_escolares_pb.csv")

st.sidebar.header("Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df["ano"].unique()), default=sorted(df["ano"].unique())[-3:])
mesos = st.sidebar.multiselect("Mesorregião", sorted(df["mesorregiao"].unique()))
muns = st.sidebar.multiselect("Município", sorted(df["municipio"].unique()))
redes = st.sidebar.multiselect("Rede", sorted(df["rede"].unique()))
etapas = st.sidebar.multiselect("Etapa", sorted(df["etapa"].unique()))

dff = filtro_df(df, anos, mesos, muns, redes, etapas)

st.title("⚖️ Equidade & Inclusão")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Paridade de gênero média (≈1 é ideal)", f"{dff['paridade_genero'].mean():.2f}")
with col2:
    st.metric("Índice de inclusão (0-1)", f"{dff['inclusao_ne_indice'].mean():.2f}")
with col3:
    st.metric("Alunos por professor", f"{dff['alunos_por_professor'].mean():.1f}")

st.divider()

left, right = st.columns(2)
with left:
    fig = px.box(dff, x="rede", y="paridade_genero", points="all", title="Paridade de gênero por Rede")
    st.plotly_chart(fig, use_container_width=True)
with right:
    fig2 = px.box(dff, x="mesorregiao", y="inclusao_ne_indice", points="all", title="Inclusão por Mesorregião")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
fig3 = px.scatter(dff, x="alunos_por_professor", y="media_proficiencia", color="etapa",
                  title="Alunos por Professor × Proficiência Média",
                  hover_data=["nome_escola","municipio","ano"])
st.plotly_chart(fig3, use_container_width=True)
