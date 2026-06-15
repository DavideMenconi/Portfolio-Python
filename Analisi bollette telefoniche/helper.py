def tempo_valido(colonna_tempo):
    parti = colonna_tempo.str.split(":", expand=True).astype(int)

    giorno_valido = (parti[0] >= 1) & (parti[0] <= 31)
    ora_valida = (parti[1] >= 0) & (parti[1] <= 23)
    minuti_validi = (parti[2] >= 0) & (parti[2] <= 59)

    return giorno_valido & ora_valida & minuti_validi


def converti_in_minuti(colonna_tempo):
    parti = colonna_tempo.str.split(":", expand=True).astype(int)

    return parti[0] * 24 * 60 + parti[1] * 60 + parti[2]
