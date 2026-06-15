# Progetto Bibliosoftware

## Descrizione

**Progetto Bibliosoftware** è un'applicazione Python da terminale che simula la gestione di una piccola biblioteca.

Il programma permette di:

- visualizzare i libri presenti;
- aggiungere nuovi libri;
- aggiornare le copie di un libro già esistente;
- rimuovere un libro;
- verificare la disponibilità di un titolo;
- prendere in prestito una copia;
- restaurare o aggiungere nuove copie;
- calcolare statistiche generali sulla biblioteca.

Il progetto è stato sviluppato come esercizio pratico per consolidare le basi di Python, l'uso delle liste di dizionari e una prima introduzione all'utilizzo di `pandas`.

## Funzionalità principali

### 1. Visualizzazione dei libri

Mostra l'elenco dei libri presenti nella biblioteca, con informazioni su:

- titolo;
- copie totali;
- copie disponibili;
- copie prestate.

### 2. Aggiunta di un libro

La funzione `aggiungi_libro()` permette di aggiungere un nuovo libro alla biblioteca.

Se il libro è già presente, il programma non crea duplicati, ma aggiorna il numero di copie totali e disponibili.

### 3. Rimozione di un libro

La funzione `rimuovi_libro()` elimina un libro dalla biblioteca se il titolo è presente.

### 4. Verifica disponibilità

La funzione `verifica_disponibilita()` restituisce `True` se almeno una copia del libro è disponibile, altrimenti restituisce `False`.

### 5. Prestito di un libro

La funzione `prendi_in_prestito()` riduce di una unità le copie disponibili e aumenta le copie prestate.

### 6. Aggiunta/restauro copie

La funzione `restaurare_libro()` permette di aggiungere nuove copie a un libro già presente.

### 7. Statistiche biblioteca

La funzione `statistiche_biblioteca()` restituisce un dizionario con:

- numero totale di titoli;
- numero totale di copie;
- media copie per libro;
- copie disponibili;
- copie prestate.

### 8. Validazione delle copie

Il programma controlla che il numero di copie inserito sia maggiore di zero, evitando valori incoerenti come `0` o numeri negativi.

