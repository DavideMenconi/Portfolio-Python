import pandas as pd
from helper import converti_in_minuti, tempo_valido

def ottieniDatiTelefonate(file):
    df = pd.read_csv(file, sep=";")

    df["Cod_Chiamante"] = (
        df["Cod_Chiamante"]
        .astype(str)
        .str.replace("#", "", regex=False)
        .str.strip()
        .astype(int)
    )

    df = df[tempo_valido(df["Inizio"]) & tempo_valido(df["Fine"])].copy()

    df["Inizio"] = converti_in_minuti(df["Inizio"])
    df["Fine"] = converti_in_minuti(df["Fine"])

    df["Minuti_di_Conversazione"] = df["Fine"] - df["Inizio"] + 1

    df = df[df["Minuti_di_Conversazione"] > 0].copy()
    df = df[df["Minuti_di_Conversazione"] <= 600].copy()

    df = df[df["Cod_Chiamante"] != df["Cod_Destinatario"]].copy()

    lista_telefonate = list(zip(
        df["Cod_Chiamante"].astype(int),
        df["Cod_Destinatario"].astype(int),
        df["Cod_Cella_Chiamante"].astype(int),
        df["Cod_Cella_Destinatario"].astype(int),
        df["Minuti_di_Conversazione"].astype(int)
    ))

    return lista_telefonate
    
def calcolaBollette(file):
    datiChiamate = ottieniDatiTelefonate(file)

    df_new = pd.DataFrame(datiChiamate, columns=["Cod_Chiamante", "Cod_Destinatario", "Cod_Cella_Chiamante", "Cod_Cella_Destinatario", "Minuti_di_Conversazione"])

    df_bolletta = df_new.groupby("Cod_Chiamante")[["Minuti_di_Conversazione"]].sum().reset_index()

    df_bolletta["Minuti_a_Pagamento"] = df_bolletta["Minuti_di_Conversazione"] - 20

    df_bolletta.loc[df_bolletta["Minuti_a_Pagamento"] < 0, "Minuti_a_Pagamento"] = 0

    df_bolletta["Costo_Chiamate"] = df_bolletta["Minuti_a_Pagamento"] * 0.10

    dizionario_costi = {}

    for riga in range(len(df_bolletta)):
        codice_chiamante = int(df_bolletta.loc[riga, "Cod_Chiamante"])
        costo_chiamate = round(float(df_bolletta.loc[riga, "Costo_Chiamate"]), 2)

        dizionario_costi[codice_chiamante] = costo_chiamate

    return dizionario_costi

def calcolaCelleCongestionate(file):

  datiChiamate = ottieniDatiTelefonate(file)

  df2 = pd.DataFrame(datiChiamate, columns=["Cod_Chiamante", "Cod_Destinatario", "Cod_Cella_Chiamante", "Cod_Cella_Destinatario", "Minuti_di_Conversazione"])

  df2["Numero_telefonate"] = 1

  df_celle = df2.groupby("Cod_Cella_Chiamante")[["Numero_telefonate"]].sum().reset_index()

  media_telefonate = df_celle["Numero_telefonate"].mean()

  df_celle["Congestione"] = df_celle["Numero_telefonate"] > media_telefonate

  celle_congestionate = []

  for riga in range(len(df_celle)):
     if df_celle.loc[riga, "Congestione"] == True:
         codice_cella = int(df_celle.loc[riga, "Cod_Cella_Chiamante"])
         celle_congestionate.append(codice_cella)

  return(celle_congestionate)

def main ():
  file = input("Inserisci il nome del file CSV: ")

  dati_telefonate = ottieniDatiTelefonate(file)
  bollette = calcolaBollette(file)
  celle_congestionate = calcolaCelleCongestionate(file)

  print(f'Dati telefonate: {dati_telefonate}')
  print(f"Bollette calcolate: {bollette}")
  print(f"Celle congestionate: {celle_congestionate}")

main()
