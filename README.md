# Calcolo-della-bolletta-telefonica
Progetto a tema Data Analytics

Il file “telefonate.csv” contiene informazioni sulle telefonate effettuate in un mese da alcuni clienti di un operatore di telefonia cellulare.

Funzione ottieniDatiTelefonate. La funzione accetta come unico parametro in ingresso il nome del file con i dati sulle telefonate effettuate. La funzione restituisce una lista formata da tuple, dove ogni tupla contiene i seguenti dati (ogni tupla corrisponde ad una telefonata): (Cod_Chiamante, Cod_Destinatario, Cod_Cella_Chiamante, Cod_Cella_Destinatario, Numeo_Minuti_Di_Conversazione).

Funzione calcolaBollette. La funzione accetta come parametro in ingresso la struttura dati restituita dalla funzione precedente. 
La funzione dovra' restituire un dizionario di coppie chiave valore  in cui la chiave e' il codice del cliente e il valore e' un float corrispondente all'importo che il cliente deve pagare per le chiamate effettuate nel mese. La tariffazione delle chiamate avviene sulla base dei minuti di conversazione, un cliente paga 0.10 euro (10 centesimi di euro) per ogni minuto di chiamata effettuata. 
Il cliente che riceve la chiamata non paga niente. Ogni cliente ha un bonus di 20 minuti gratuiti al mese, quindi il cliente paghera' solamente per i minuti eccedenti il bonus. 
L'insieme dei clienti contenuti nel dizionario e' formato da quei clienti che appaiono almeno una volta come chiamanti nella struttura dati fornita in ingresso.

Funzione calcolaCelleCongestionate. La funzione accetta come parametro in ingresso la struttura dati creata dalla funzione ottieniDatiTelefonate. La funzione deve identificare le celle (cioe' le aree) che hanno un elevato carico di telefonate. 
Sono congestionate le celle nelle quali il numero di telefonate effettuate è maggiore alla media.
La funzione restituisce una lista con i codici delle celle congestionate.


