# Laboratorio di _Introduzione alle Applicazioni Web_

## Laboratorio #1: Primi passi con HTML5

Realizzare il mock-up utilizzando HTML5 (senza aggiungere stile alla pagina).

## Laboratorio #2: Primi passi con CSS3

Aggiungere uno stile alla pagina tramite CSS3, utilizzando le proprietà di _float_ e _position_.

## Laboratorio #3: CSS Avanzato

-   [x] Aggiungere uno stile alla pagina tramite CSS3, utilizzando il layout _flexbox_ (al posto della proprietà _float_);
-   [x] Rendere il layout _responsive_, utilizzando delle apposite media queries. Il layout dell’applicazione, in particolare, dovrà adattarsi automaticamente per essere visualizzato su tablet e su smartphone.

## Laboratorio #4: Bootstrap

Applicare il framework Bootstrap alla homepage.

-   [x] Importare Bootstrap nella pagina web attraverso gli opportuni tag \<meta\>, \<link\> e \<script\>;
-   [x] Implementare il layout della pagina sfruttando il grid system offerto da Bootstrap;
-   [x] Rendere il layout dell'applicazione responsive attraverso i breakpoint definiti da Bootstrap.

## Laboratorio #5: Flask

Creare un back-end in Python per il social network sviluppato durante il laboratorio, utilizzando il framework Flask.

-   [x] Creare una nuova pagina HTML “Chi siamo”. La pagina conterrà testo e immagini statiche che descrivono voi come sviluppatori unici vostro social network. Per lo stile della pagina, continuate ad utilizzare Bootstrap.
-   [x] Creare una applicazione Flask che includa un decoratore (e la relativa funzione) per l’homepage del social network, e un decoratore (e la relativa funzione) per la pagina “Chi siamo”.
-   [x] Definire una serie di post da visualizzare nella homepage, utilizzando una opportuna struttura dati. Ad esempio, ogni post potrebbe essere un dizionario con le seguenti informazioni:
    -   Nickname;
    -   Data di pubblicazione;
    -   Testo principale;
    -   Il percorso su disco dell'immagine di profilo;
    -   Il percorso su disco dell'immagine del post, se presente.
-   [x] Utilizzare il motore di templating Jinja per servire le pagine web (homepage e “Chi siamo”) mantenendo la struttura dell’HTML separata dai dati gestiti dall’applicazione. Occorre:
    -   Creare le cartelle necessarie all’interno del progetto, inserendo i file HTML all’interno della cartella “templates”;
    -   Modificare il file HTML sviluppato nei precedenti laboratori, eliminando i post statici e sostituendoli con le opportune espressioni e statement di programmazione. Nello stesso file, inserire un link verso la nuova pagina “Chi siamo” all’interno della navbar.
    -   Adattare il file HTML per “Chi siamo” in modo da sfruttare le espressioni di Jinja per le immagini ed eventuali link.

## Laboratorio #6: Flask Avanzato

Estendere il social network aggiungendo la possibilità di visualizzare i singoli post in una pagina dedicata, sfruttando le route dinamiche di Flask e il templating di Jinja.

-   [x] Associare un identificativo numerico univoco ai post salvati nell'applicazione, aggiungendo un opportuno campo alle strutture dati utilizzate;
-   [x] Creare una route dinamica per i singoli post, utilizzando gli identificativi numerici dei post come parametro. Quando l'utente clicca sul post nella homepage, il sito web mostra una pagina dedicata dove viene visualizzato il post selezionato. La pagina in questione dovrà avere la stessa struttura della homepage (navbar, aside...), e dovrà visualizzare tutte le informazioni del post nel corpo principale;
-   [x] Ristrutturare il codice HTML dell'intera applicazione utilizzando l'ereditarietà dei template offerta da jinja. Si definisca un template di base che includa la navbar e l'aside, e lo si riutilizzi estendendolo in tutte le pagine del sito web.

## Laboratorio #7: Form e Sessioni

Implementare un meccanismo (rudimentale) di autenticazione, e aggiungere la possibilità di creare nuovi post da visualizzare nella home page.

-   [x] Alla prima apertura del social, l'utente non è ancora autenticato, e non ha la possibilità di creare nuovi post. Per permettere l'autenticazione, aggiungere un bottone _Autenticati!_ alla navbar;
-   [x] Alla pressione del bottone _Autenticati!_, aprire un modale Bootstrap e permettere all'utente di selezionare, tramite opportuno form, uno degli username. Al click del bottone _Salva_, salvare lo username selezionato nella sessione corrente;
-   [x] Quando un utente è autenticato, la navbar visualizza un messaggio di benvenuto, il bottone _+_ diventa visibile, e i post dell'utente vengono evidenziati con uno sfondo colorato;
-   [x] Alla pressione del bottote _+_, permettere all'utente (autenticato) di creare un nuovo post. In particolare, aprire un modale Bootstrap contenente un form con i seguenti campi:
    -   Un campo di testo (disabilitato e precompilato) con lo username dell'utente;
    -   Un' area di testo per inserire il testo del post (obbligatorio) con il suggerimento _Inserisci un testo per il tuo post_, una lunghezza minima di 30 caratteri e una massima di 200;
    -   Un campo per l'upload dell'immagine del post (opzionale);
    -   Un campo per selezionare la data del post (obbligatorio), la data deve essere posteriore o uguale alla data corrente.
        All'invio del form, la relativa route in Flask si occuperà di aggiungere il post nell'apposita struttura dati, e visualizzerà la lista di post aggiornata nella home page.

## Laboratorio #8: Database

Rendere persistenti i dati del social network attraverso l'utilizzo di un databse, aggiungendo la possibilità da parte degli utenti di lasciare commenti ai post.

-   [ ] Creare un database SQLite, che dovrà avere tre tabelle, opportunamente collegate tra loro:
    -   [ ] Tabella _UTENTI_(**id**, nickname, password, immagine*profilo). Il campo \_id* sarà univoco per ogni utente, e fungerà da chiave primaria. Il campo _immagine_profilo_ conterrà il percorso su disco dell'immagine di profilo dell'utente;
    -   [ ] Tabella _POST_(**id**, data*pubblicazione, testo, immagine_post\*, id_utente). Il campo numerico \_id* sarà univoco per ogni post,e fungerà da chiave primaria. Il campo _immagine_profilo_ (opzionale) conterrà il percorso su disco dell'immagine del post. Il campo numerico _id_utente_ sarà la chiave esterna che permettera di collegare un post all'utente che lo ha creato;
    -   [ ] Tabella _COMMENTI_(**id**, data*pubblicazione, testo, id_post, id_utente). Il campo numerico \_id* sarà univoco per ogni post, e fungerà da chiave primaria. I campi numerici _id_post_ e _id_utente_ saranno le chiave esterne che permettono di collegare un commento al suo post e all'utente che lo ha inserito.
-   [ ] Includere il database creato nel progetto, e modificare il codice dell'applicazione affinché i post visualizzati dal social network siano recuperati dal databse (creare un file separato che contiene tutte le informazioni per accedere al database);
-   [ ] Modificare l'applicazione in modo che la creazione di un nuovo post utilizzi il database per salvare le informazioni;
-   [ ] Nella pagina di dettaglio dei singoli post, aggiungere la possibilità per gli utenti autenticati di lasciare del commenti. Occorre aggiungere un form per la creazione dei commenti, composto da una singola area di test ed un bottone _'Invia'_. Tale form non sarà visibile per gli utenti non autenticati. La stessa pagina di dettaglio mostrerà anche tutti i commenti già presenti per il post in questione, visualizzandone l'autore, il testo e la data di creazione. La lista dei commenti sarà visibile sempre, anche per gli utenti non autenticati.
