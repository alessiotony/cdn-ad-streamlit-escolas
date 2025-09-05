# Painel Educacional PB — Streamlit (Fictício)

Um app **moderno** em Streamlit com dados **sintéticos** de escolas da Paraíba (PB).
Inclui múltiplas páginas, filtros, KPIs, gráficos e mapa.

## Como rodar

```bash
python3 -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura

```
streamlit_escolas_pb/
├── app.py
├── utils.py
├── data/
│   └── indicadores_escolares_pb.csv
├── pages/
│   ├── 01_Visao_Geral.py
│   ├── 02_Explorador_de_Escolas.py
│   ├── 03_Equidade_e_Inclusao.py
│   ├── 04_Mapa.py
│   └── 05_Sobre_os_Dados.py
└── .streamlit/
    └── config.toml
```
