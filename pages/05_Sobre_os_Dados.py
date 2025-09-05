import streamlit as st

st.set_page_config(page_title="Sobre os Dados • Painel Educacional PB", page_icon="ℹ️", layout="wide")

st.title("ℹ️ Sobre os Dados")
st.markdown(
    """
    **Origem:** os dados deste painel são inteiramente **sintéticos**. Foram gerados com distribuições aleatórias
    calibradas para lembrar ordens de grandeza observadas em bases educacionais, **sem** corresponder a escolas reais.

    **Adaptação para dados reais:**
    1. Substitua `data/indicadores_escolares_pb.csv` por seu dataset.
    2. Ajuste mapeamentos de colunas em `utils.py` caso os nomes mudem.
    3. Revise filtros e gráficos nas páginas conforme a disponibilidade dos indicadores.

    **Indicadores (exemplos):**
    - `ideb`: índice de desenvolvimento da educação básica (0–10).
    - `taxa_aprovacao` e `taxa_evasao`: em porcentagem.
    - `professores_por_aluno` e `alunos_por_professor`: proxies de atendimento.
    - `infraestrutura_indice`, `internet_mbps`, `inclusao_ne_indice`, `paridade_genero`.
    - `prof_math`, `prof_port` e `media_proficiencia`.

    **Licença:** uso livre para fins acadêmicos e prototipagem.
    """
)
