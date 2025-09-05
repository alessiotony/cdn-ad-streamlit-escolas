import streamlit as st
import pandas as pd
import pydeck as pdk
from utils import load_data, filtro_df

st.set_page_config(page_title="Mapa • Painel Educacional PB", page_icon="🗺️", layout="wide")

df = load_data("data/indicadores_escolares_pb.csv")

st.sidebar.header("Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df["ano"].unique()), default=[df["ano"].max()])
mesos = st.sidebar.multiselect("Mesorregião", sorted(df["mesorregiao"].unique()))
muns = st.sidebar.multiselect("Município", sorted(df["municipio"].unique()))
redes = st.sidebar.multiselect("Rede", sorted(df["rede"].unique()))
etapas = st.sidebar.multiselect("Etapa", sorted(df["etapa"].unique()))

dff = filtro_df(df, anos, mesos, muns, redes, etapas)

st.title("🗺️ Mapa das Escolas")

tooltip = {
    "html": "<b>{nome_escola}</b><br/>{municipio} - {rede}<br/>IDEB: {ideb}<br/>Aprovação: {taxa_aprovacao}%",
    "style": {"backgroundColor": "steelblue", "color": "white"}
}
layer = pdk.Layer(
    "ScatterplotLayer",
    data=dff,
    get_position='[lon, lat]',
    get_fill_color='[30, 144, 255, 160]',
    get_radius=2000,
    pickable=True,
    radius_min_pixels=4,
    radius_max_pixels=20,
)
view_state = pdk.ViewState(latitude=float(dff["lat"].mean()), longitude=float(dff["lon"].mean()), zoom=7)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))
st.caption("Pontos são aproximados e **fictícios**, usados apenas para demonstração.")
