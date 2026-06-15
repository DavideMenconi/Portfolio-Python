# Progetto Classifica Campionato

## Descrizione

**Progetto Classifica Campionato** è un'applicazione Python da terminale che analizza i risultati di un campionato di calcio e calcola le principali informazioni statistiche delle squadre.

Il programma permette di:

- calcolare il totale dei punti di una squadra;
- calcolare vittorie, pareggi e sconfitte di una squadra;
- creare e stampare il dizionario della classifica;
- verificare che la squadra inserita dall'utente sia presente nei dati;
- organizzare il programma con funzioni ordinate e un `main()` leggero.

Il progetto è stato sviluppato come esercizio pratico per consolidare le basi di Python, in particolare l'uso di tuple, liste, dizionari, funzioni, condizioni e cicli.

---

## Obiettivi del progetto

Questo progetto ha l'obiettivo di esercitare:

- la gestione di dati strutturati con liste di tuple;
- l'utilizzo dei dizionari per memorizzare dati aggregati;
- la creazione di funzioni con responsabilità specifiche;
- il controllo dell'esistenza di una chiave in un dizionario;
- l'organizzazione corretta di uno script Python;
- la scrittura di un `main()` semplice e ordinato.

---

## Funzionalità principali

### 1. Calcolo dei punti

La funzione `totale_punti(nome)` calcola il totale dei punti ottenuti da una squadra alla fine del campionato.

La logica applicata è:

- vittoria: 3 punti;
- pareggio: 1 punto;
- sconfitta: 0 punti.

### 2. Calcolo del rendimento

La funzione `rendimento(squadra)` calcola:

- numero di vittorie;
- numero di pareggi;
- numero di sconfitte.

Il risultato viene restituito sotto forma di messaggio leggibile.

### 3. Creazione e stampa della classifica

La funzione `stampa_classifica()` crea il dizionario della classifica e lo stampa a schermo.

La classifica non viene ordinata, perché l'obiettivo dell'esercizio è mostrare i dati così come vengono calcolati, senza utilizzare criteri di ordinamento avanzati.

---

## Struttura del codice

Il programma è organizzato secondo l'ordine corretto di uno script Python:

```python
# dati iniziali

def totale_punti(nome):
    ...

def rendimento(squadra):
    ...

def stampa_classifica():
    ...

def main():
    ...

main()
```

Questa struttura rende il codice più leggibile e più facile da mantenere.

---

## Correzioni implementate

Durante la revisione del progetto sono state applicate alcune correzioni importanti:

### Controllo corretto delle squadre nei dizionari

Invece di usare una logica del tipo:

```python
if squadra1 not in classifica or squadra2 not in classifica:
```

è stata utilizzata una soluzione più sicura:

```python
for squadra in p[1:3]:
    if squadra not in classifica:
        classifica[squadra] = 0
```

In questo modo viene controllata una squadra alla volta, evitando di sovrascrivere dati già calcolati.

### Main più leggero

Il `main()` non contiene più un ciclo infinito. Il programma richiede semplicemente:

1. una squadra per visualizzare il totale dei punti;
2. una squadra per visualizzare il rendimento;
3. la stampa finale della classifica.

### Rimozione dell'ordinamento non richiesto

La classifica viene mostrata come dizionario calcolato, senza usare `sorted()` o criteri di ordinamento non necessari.

---

## Requisiti

Il progetto utilizza solo Python standard.

Non sono richieste librerie esterne.

---

## Come eseguire il progetto

Dopo aver clonato o scaricato la repository, entra nella cartella del progetto ed esegui:

```bash
python main.py
```

Il programma chiederà due input:

```text
Inserisci la squadra per vedere i punti:
Inserisci la squadra per vedere il rendimento:
```

Infine stamperà il dizionario della classifica.

---

## Esempio di utilizzo

```text
Inserisci la squadra per vedere i punti: Inter
La squadra Inter ha conseguito 84 punti alla fine del campionato.

Inserisci la squadra per vedere il rendimento: Milan
N. vittorie 22, N. pareggi 8, N. sconfitte 8.

{'Udinese': 58, 'Palermo': 57, ...}
```

---

## Competenze dimostrate

Questo progetto dimostra competenze di base in:

- Python;
- liste;
- tuple;
- dizionari;
- funzioni;
- cicli `for`;
- condizioni `if`, `elif`, `else`;
- validazione semplice degli input;
- organizzazione di un programma con `main()`.

---

## Possibili miglioramenti futuri

Alcuni miglioramenti possibili sono:

- leggere i risultati da un file CSV;
- salvare la classifica su file;
- aggiungere statistiche sui gol fatti e subiti;
- ordinare la classifica quando l'argomento sarà stato trattato;
- aggiungere test automatici;
- trasformare il progetto in una piccola applicazione con menu.
