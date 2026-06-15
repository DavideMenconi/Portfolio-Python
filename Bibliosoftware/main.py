import pandas as pd

libri = [
    {"titolo": "Il nome della rosa", "copie_totali": 3, "copie_disponibili": 3, "copie_prestate": 0},
    {"titolo": "1984", "copie_totali": 5, "copie_disponibili": 5, "copie_prestate": 0},
    {"titolo": "Il piccolo principe", "copie_totali": 4, "copie_disponibili": 4, "copie_prestate": 0},
    {"titolo": "Se questo è un uomo", "copie_totali": 2, "copie_disponibili": 2, "copie_prestate": 0},
    {"titolo": "La coscienza di Zeno", "copie_totali": 3, "copie_disponibili": 3, "copie_prestate": 0},
    {"titolo": "I promessi sposi", "copie_totali": 6, "copie_disponibili": 6, "copie_prestate": 0},
    {"titolo": "Orgoglio e pregiudizio", "copie_totali": 2, "copie_disponibili": 2, "copie_prestate": 0},
    {"titolo": "Il signore degli anelli", "copie_totali": 4, "copie_disponibili": 4, "copie_prestate": 0},
    {"titolo": "Harry Potter e la pietra filosofale", "copie_totali": 7, "copie_disponibili": 7, "copie_prestate": 0},
    {"titolo": "Delitto e castigo", "copie_totali": 3, "copie_disponibili": 3, "copie_prestate": 0}
]

# ##aggiungi_libro(titolo, copie)
# Descrizione: Aggiunge un nuovo libro alla biblioteca con il numero di copie specificato.
# Se il libro esiste già, aggiorna il numero di copie aggiungendo quelle nuove.
# Se il libro non esiste, lo aggiunge al sistema.
def aggiungi_libro(titolo, copie):
    if copie <= 0:
        print("Il numero di copie deve essere maggiore di zero.")
        return

    for libro in libri:
        if libro["titolo"] == titolo:
            libro["copie_totali"] += copie
            libro["copie_disponibili"] += copie
            print(f"Il libro '{titolo}' esiste già. Sono state aggiunte {copie} copie.")
            return

    nuovo_libro = {
        "titolo": titolo,
        "copie_totali": copie,
        "copie_disponibili": copie,
        "copie_prestate": 0
    }

    libri.append(nuovo_libro)
    print(f"Libro '{titolo}' aggiunto correttamente.")


# ##rimuovi_libro(titolo)
# Descrizione: Rimuove un libro dalla biblioteca.
# Se il libro esiste, viene eliminato dal sistema.
# Se il libro non esiste, il programma stampa un messaggio di errore.

def rimuovi_libro(titolo):
    for libro in libri:
        if libro["titolo"] == titolo:
            libri.remove(libro)
            print(f"Libro '{titolo}' rimosso correttamente.")
            return

    print(f"Il libro '{titolo}' non esiste.")


# ##verifica_disponibilita(titolo)
# Descrizione: Controlla se un libro è disponibile nella biblioteca.
# Restituisce True se almeno una copia è disponibile.
# Restituisce False se il libro non esiste o non ci sono copie disponibili.

def verifica_disponibilita(titolo):
    for libro in libri:
        if libro["titolo"] == titolo:
            return libro["copie_disponibili"] > 0

    return False


# ## prendi_in_prestito(titolo)
# Descrizione: Riduce il numero di copie disponibili di un libro di 1, simulando un prestito:
# Se il libro è disponibile, decrementa il numero di copie di 1.
# Se non ci sono copie disponibili o il libro non esiste, stampa un messaggio di errore.
#

def prendi_in_prestito(titolo):
    for libro in libri:
        if libro["titolo"] == titolo:
            if libro["copie_disponibili"] > 0:
                libro["copie_disponibili"] -= 1
                libro["copie_prestate"] += 1
                print(f"Libro '{titolo}' preso in prestito.")
            else:
                print("Sono stati prestati tutti i libri.")
            return

    print("Libro non disponibile.")


# ## statistiche_biblioteca()
# Descrizione: Restituisce un dizionario con informazioni sulla biblioteca.
# totale_libri: numero totale di titoli.
# copie_totali: numero totale di copie.
# media_copie: numero medio di copie per libro.

def statistiche_biblioteca():
    df = pd.DataFrame(libri)

    statistiche = {
        "totale_libri": int(df["titolo"].count()),
        "copie_totali": int(df["copie_totali"].sum()),
        "media_copie": float(df["copie_totali"].mean()),
        "copie_disponibili": int(df["copie_disponibili"].sum()),
        "copie_prestate": int(df["copie_prestate"].sum())
    }

    return statistiche


# ## visualizza_libri()
# Descrizione: Mostra un elenco di tutti i libri nella biblioteca insieme al numero di copie disponibili.
# Se la biblioteca è vuota, stampa un messaggio che indica che non ci sono libri.

def visualizza_libri():
    if not libri:
        print("La biblioteca è vuota.")
    else:
        df = pd.DataFrame(libri)
        print(df)


# ## restaurare_libro(titolo, copie)
# Descrizione: Ripristina (aggiunge) copie di un libro che è stato preso in prestito o che necessita di più copie.
# Se il libro esiste, aggiunge il numero specificato di copie.
# Se il libro non esiste, stampa un messaggio di errore.
#

def restaurare_libro(titolo, copie):
    if copie <= 0:
        print("Il numero di copie deve essere maggiore di zero.")
        return

    for libro in libri:
        if libro["titolo"] == titolo:
            libro["copie_totali"] += copie
            libro["copie_disponibili"] += copie
            print(f"Sono state aggiunte {copie} copie al libro '{titolo}'.")
            return

    print("Il libro non è presente in biblioteca.")


# ## Main

def main():
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Visualizza libri")
        print("2. Aggiungi libro")
        print("3. Rimuovi libro")
        print("4. Verifica disponibilità")
        print("5. Prendi in prestito")
        print("6. Restaura/Aggiungi copie")
        print("7. Statistiche biblioteca")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            visualizza_libri()

        elif scelta == "2":
            titolo = input("Inserisci il titolo del libro: ")
            copie = int(input("Inserisci il numero di copie: "))
            aggiungi_libro(titolo, copie)

        elif scelta == "3":
            titolo = input("Inserisci il titolo del libro da rimuovere: ")
            rimuovi_libro(titolo)

        elif scelta == "4":
            titolo = input("Inserisci il titolo del libro da verificare: ")
            disponibile = verifica_disponibilita(titolo)

            if disponibile:
                print("Il libro è disponibile.")
            else:
                print("Il libro non è disponibile o non esiste.")

        elif scelta == "5":
            titolo = input("Inserisci il titolo del libro da prendere in prestito: ")
            prendi_in_prestito(titolo)

        elif scelta == "6":
            titolo = input("Inserisci il titolo del libro da restaurare: ")
            copie = int(input("Quante copie vuoi aggiungere? "))
            restaurare_libro(titolo, copie)

        elif scelta == "7":
            statistiche_biblioteca()

        elif scelta == "0":
            print("Programma terminato.")
            break

        else:
            print("Scelta non valida. Riprova.")


main()


# ##
