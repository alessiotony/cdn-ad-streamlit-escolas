import streamlit as st
from utils import load_data

st.set_page_config(page_title="Painel Educacional PB", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
    .kpi-card {background: var(--secondary-background-color); border-radius: 14px; padding: 18px; border: 1px solid #eaecef;}
    .muted {color: #64748B; font-size: 0.9rem;}
    </style>
    """, unsafe_allow_html=True
)

st.title("🎓 Indicadores Educacionais — Paraíba (Fictícios)")
st.caption("Protótipo interativo em Streamlit • dados sintéticos para demonstração")

st.write("Use o menu lateral para navegar entre as páginas.")

st.subheader("O que você encontra aqui?")
st.markdown(
    """
    - **Visão Geral** com KPIs e tendências temporais.
    - **Explorador de Escolas** com busca, filtros e tabela exportável.
    - **Equidade & Inclusão** com cortes por gênero e necessidades educacionais.
    - **Mapa** das escolas com indicadores-chave.
    - **Sobre os Dados** explicando a geração sintética e como adaptar para dados reais.
    """
)

st.info("Dica nerd: este projeto já acompanha `requirements.txt` e uma base CSV em `data/`. É só instalar e rodar `streamlit run app.py`.")
