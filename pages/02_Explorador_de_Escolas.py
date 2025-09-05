import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, filtro_df

st.set_page_config(page_title="Explorador de Escolas • Painel Educacional PB", page_icon="🏫", layout="wide")

df = load_data("data/indicadores_escolares_pb.csv")

st.sidebar.header("Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df["ano"].unique()), default=[df["ano"].max()])
mesos = st.sidebar.multiselect("Mesorregião", sorted(df["mesorregiao"].unique()))
muns = st.sidebar.multiselect("Município", sorted(df["municipio"].unique()))
redes = st.sidebar.multiselect("Rede", sorted(df["rede"].unique()))
etapas = st.sidebar.multiselect("Etapa", sorted(df["etapa"].unique()))

dff = filtro_df(df, anos, mesos, muns, redes, etapas)

st.title("🏫 Explorador de Escolas")
st.caption("Pesquise por nome, ordene colunas e exporte o resultado.")

q = st.text_input("Buscar por nome da escola:", "")
if q:
    dff = dff[dff["nome_escola"].str.contains(q, case=False, na=False)]

st.subheader("Ranking por IDEB (top 20 no filtro atual)")
rank = (dff.sort_values(["ano","ideb"], ascending=[False, False])
          .groupby("nome_escola").head(1)
          .sort_values("ideb", ascending=False)
          .head(20))
st.dataframe(rank[["ano","municipio","rede","etapa","ideb","taxa_aprovacao","taxa_evasao","media_proficiencia"]])

st.divider()
fig = px.scatter(dff, x="ideb", y="taxa_evasao", color="municipio",
                 hover_data=["nome_escola","rede","etapa","ano"],
                 title="IDEB × Evasão por Escola")
st.plotly_chart(fig, use_container_width=True)

csv = dff.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Baixar dados filtrados (CSV)", data=csv, file_name="escolas_filtradas.csv", mime="text/csv")
