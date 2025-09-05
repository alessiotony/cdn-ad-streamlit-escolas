import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["alunos_por_professor"] = (1 / df["professores_por_aluno"]).round(1)
    df["media_proficiencia"] = ((df["prof_math"] + df["prof_port"]) / 2).round(2)
    return df

def filtro_df(df, ano, meso, municipio, rede, etapa):
    dff = df.copy()
    if ano:
        dff = dff[dff["ano"].isin(ano)]
    if meso:
        dff = dff[dff["mesorregiao"].isin(meso)]
    if municipio:
        dff = dff[dff["municipio"].isin(municipio)]
    if rede:
        dff = dff[dff["rede"].isin(rede)]
    if etapa:
        dff = dff[dff["etapa"].isin(etapa)]
    return dff
