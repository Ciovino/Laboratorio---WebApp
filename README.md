# Laboratorio di *Introduzione alle Applicazioni Web*

## Laboratorio #1: Primi passi con HTML5
Realizzare il mock-up utilizzando HTML5 (senza aggiungere stile alla pagina).

## Laboratorio #2: Primi passi con CSS3
Aggiungere uno stile alla pagina tramite CSS3, utilizzando le proprietà di *float* e *position*.

## Laboratorio #3: CSS Avanzato
[x] Aggiungere uno stile alla pagina tramite CSS3, utilizzando il layout *flexbox* (al posto della proprietà *float*);
[x] Rendere il layout *responsive*, utilizzando delle apposite media queries. Il layout dell’applicazione, in particolare, dovrà adattarsi automaticamente per essere visualizzato su tablet e su smartphone.

## Laboratorio #4: Bootstrap
Applicare il framework Bootstrap alla homepage.
[x] Importare Bootstrap nella pagina web attraverso gli opportuni tag \<meta\>, \<link\> e \<script\>;
[x] Implementare il layout della pagina sfruttando il grid system offerto da Bootstrap;
[x] Rendere il layout dell'applicazione responsive attraverso i breakpoint definiti da Bootstrap.

## Laboratorio #5: Flask
Creare un back-end in Python per il social network sviluppato durante il laboratorio, utilizzando il framework Flask.
[x] Creare una nuova pagina HTML “Chi siamo”. La pagina conterrà testo e immagini statiche che descrivono voi come sviluppatori unici vostro social network. Per lo stile della pagina, continuate ad utilizzare Bootstrap.
[x] Creare una applicazione Flask che includa un decoratore (e la relativa funzione) per l’homepage del social network, e un decoratore (e la relativa funzione) per la pagina “Chi siamo”.
[x] Definire una serie di post da visualizzare nella homepage, utilizzando una opportuna struttura dati. Ad esempio, ogni post potrebbe essere un dizionario con le seguenti informazioni: 
  - Nickname;
  - Data di pubblicazione;
  - Testo principale;
  - Il percorso su disco dell'immagine di profilo;
  - Il percorso su disco dell'immagine del post, se presente.
[x] Utilizzare il motore di templating Jinja per servire le pagine web (homepage e “Chi siamo”) mantenendo la struttura dell’HTML separata dai dati gestiti dall’applicazione. Occorre:
  - Creare le cartelle necessarie all’interno del progetto, inserendo i file HTML all’interno della cartella “templates”;
  - Modificare il file HTML sviluppato nei precedenti laboratori, eliminando i post statici e sostituendoli con le opportune espressioni e statement di programmazione. Nello stesso file, inserire un link verso la nuova pagina “Chi siamo” all’interno della navbar.
  - Adattare il file HTML per “Chi siamo” in modo da sfruttare le espressioni di Jinja per le immagini ed eventuali link.

## Laboratorio #6: Flask Avanzato
Estendere il social network aggiungendo la possibilità di visualizzare i singoli post in una pagina dedicata, sfruttando le route dinamiche di Flask e il templating di Jinja.
[x] Associare un identificativo numerico univoco ai post salvati nell'applicazione, aggiungendo un opportuno campo alle strutture dati utilizzate;
[x] Creare una route dinamica per i singoli post, utilizzando gli identificativi numerici dei post come parametro. Quando l'utente clicca sul post nella homepage, il sito web mostra una pagina dedicata dove viene visualizzato il post selezionato. La pagina in questione dovrà avere la stessa struttura della homepage (navbar, aside...), e dovrà visualizzare tutte le informazioni del post nel corpo principale;
[x] Ristrutturare il codice HTML dell'intera applicazione utilizzando l'ereditarietà dei template offerta da jinja. Si definisca un template di base che includa la navbar e l'aside, e lo si riutilizzi estendendolo in tutte le pagine del sito web.
  
## Laboratorio #7: Form e Sessioni
Implementare un meccanismo (rudimentale) di autenticazione, e aggiungere la possibilità di creare nuovi post da visualizzare nella home page.
[x] Alla prima apertura del social, l'utente non è ancora autenticato, e non ha la possibilità di creare nuovi post. Per permettere l'autenticazione, aggiungere un bottone *Autenticati!* alla navbar;
[ ] Alla pressione del bottone *Autenticati!*, aprire un modale Bootstrap e permettere all'utente di selezionare, tramite opportuno form, uno degli username. Al click del bottone *Salva*, salvare lo username selezionato nella sessione corrente;
[ ] Quando un utente è autenticato, la navbar visualizza un messaggio di benvenuto, il bottone *+* diventa visibile, e i post dell'utente vengono evidenziati con uno sfondo colorato;
[ ] Alla pressione del bottote *+*, permettere all'utente (autenticato) di creare un nuovo post. In particolare, aprire un modale Bootstrap contenente un form con i seguenti campi:
  - Un campo di testo (disabilitato e precompilato) con lo username dell'utente;
  - Un' area di testo per inserire il testo del post (obbligatorio) con il suggerimento *Inserisci un testo per il tuo post*, una lunghezza minima di 30 caratteri e una massima di 200;
  - Un campo per l'upload dell'immagine del post (opzionale);
  - Un campo per selezionare la data del post (obbligatorio), la data deve essere posteriore o uguale alla data corrente.
All'invio del form, la relativa route in Flask si occuperà di aggiungere il post nell'apposita struttura dati, e visualizzerà la lista di post aggiornata nella home page.