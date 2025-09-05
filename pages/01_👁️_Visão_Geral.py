import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, filtro_df

st.set_page_config(page_title="Visão Geral • Painel Educacional PB", page_icon="📊", layout="wide")

df = load_data("data/indicadores_escolares_pb.csv")

st.sidebar.header("Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df["ano"].unique()), default=sorted(df["ano"].unique())[-3:])
mesos = st.sidebar.multiselect("Mesorregião", sorted(df["mesorregiao"].unique()))
muns = st.sidebar.multiselect("Município", sorted(df["municipio"].unique()))
redes = st.sidebar.multiselect("Rede", sorted(df["rede"].unique()))
etapas = st.sidebar.multiselect("Etapa", sorted(df["etapa"].unique()))

dff = filtro_df(df, anos, mesos, muns, redes, etapas)

st.title("📊 Visão Geral")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("IDEB médio", f"{dff['ideb'].mean():.2f}")
with col2:
    st.metric("Aprovação média (%)", f"{dff['taxa_aprovacao'].mean():.1f}")
with col3:
    st.metric("Evasão média (%)", f"{dff['taxa_evasao'].mean():.1f}")
with col4:
    st.metric("Frequência média (%)", f"{dff['frequencia'].mean():.1f}")

st.divider()

t1, t2 = st.columns(2)
with t1:
    by_year = dff.groupby("ano", as_index=False)[["ideb", "taxa_aprovacao", "taxa_evasao"]].mean()
    fig = px.line(by_year, x="ano", y=["ideb", "taxa_aprovacao"], markers=True, title="Tendências: IDEB & Aprovação (média)")
    st.plotly_chart(fig, use_container_width=True)
with t2:
    fig2 = px.line(by_year, x="ano", y="taxa_evasao", markers=True, title="Tendência: Evasão (média)")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

c1, c2 = st.columns(2)
with c1:
    fig3 = px.box(dff, x="rede", y="ideb", points="suspectedoutliers", title="Distribuição do IDEB por Rede")
    st.plotly_chart(fig3, use_container_width=True)
with c2:
    fig4 = px.scatter(dff, x="internet_mbps", y="media_proficiencia", color="etapa",
                      trendline="ols", title="Internet (Mbps) × Proficiência Média",
                      hover_data=["municipio","nome_escola"])
    st.plotly_chart(fig4, use_container_width=True)
