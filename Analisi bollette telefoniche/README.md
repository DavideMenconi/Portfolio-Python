Progetto Python per l'analisi di dati telefonici a partire da un file CSV.  
Lo script importa, pulisce e analizza un dataset di chiamate telefoniche, calcolando:

- la durata effettiva delle chiamate;
- il costo da addebitare a ciascun chiamante;
- le celle telefoniche potenzialmente congestionate.

## Output del programma

Lo script produce tre risultati principali.

### 1. Lista delle telefonate valide

Restituisce una lista di tuple contenenti:

```text
Cod_Chiamante
Cod_Destinatario
Cod_Cella_Chiamante
Cod_Cella_Destinatario
Minuti_di_Conversazione
```

Esempio:

```python
[(101, 205, 12, 18, 6), (102, 301, 14, 16, 8)]
```
### 2. Bollette calcolate

Per ogni chiamante viene calcolato il costo complessivo delle chiamate.

La logica applicata è:

- i primi 20 minuti sono gratuiti;
- i minuti successivi costano 0,10 € al minuto;
- il risultato viene arrotondato a due decimali.

Esempio:

```python
{
    101: 2.40,
    102: 0.00,
    103: 1.70
}
```
### 3. Celle congestionate

Lo script conta il numero di chiamate effettuate da ogni cella telefonica.  
Una cella viene considerata congestionata se il numero di chiamate è superiore alla media delle chiamate per cella.

Esempio:

```python
[12, 18, 21]
```
