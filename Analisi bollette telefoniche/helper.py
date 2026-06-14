import pandas as pd


def converti_in_minuti(colonna_tempo: pd.Series) -> pd.Series:

    parti = colonna_tempo.str.split(":", expand=True).astype(int)

    return parti[0] * 24 * 60 + parti[1] * 60 + parti[2]
