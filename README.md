# Laboratorio di *Introduzione alle Applicazioni Web*

## Laboratorio #1: Primi passi con HTML5
Realizzare il mock-up utilizzando HTML5 (senza aggiungere stile alla pagina).

## Laboratorio #2: Primi passi con CSS3
Aggiungere uno stile alla pagina tramite CSS3, utilizzando le proprietà di *float* e *position*.

## Laboratorio #3: CSS Avanzato
- Aggiungere uno stile alla pagina tramite CSS3, utilizzando il layout *flexbox* (al posto della proprietà *float*);
- Rendere il layout *responsive*, utilizzando delle apposite media queries. Il layout dell’applicazione, in particolare, dovrà adattarsi automaticamente per essere visualizzato su tablet e su smartphone.

## Laboratorio #4: Bootstrap
Applicare il framework Bootstrap alla homepage.
- Importare Bootstrap nella pagina web attraverso gli opportuni tag \<meta\>, \<link\> e \<script\>;
- Implementare il layout della pagina sfruttando il grid system offerto da Bootstrap;
- Rendere il layout dell'applicazione responsive attraverso i breakpoint definiti da Bootstrap.

## Laboratorio #5: Flask
Creare un back-end in Python per il social network sviluppato durante il laboratorio, utilizzando il framework Flask.
- Creare una nuova pagina HTML “Chi siamo”. La pagina conterrà testo e immagini statiche che descrivono voi come sviluppatori unici vostro social network. Per lo stile della pagina, continuate ad utilizzare Bootstrap.
- Creare una applicazione Flask che includa un decoratore (e la relativa funzione) per l’homepage del social network, e un decoratore (e la relativa funzione) per la pagina “Chi siamo”.
- Definire una serie di post da visualizzare nella homepage, utilizzando una opportuna struttura dati. Ad esempio, ogni post potrebbe essere un dizionario con le seguenti informazioni: 
  - Nickname;
  - Data di pubblicazione;
  - Testo principale;
  - Il percorso su disco dell'immagine di profilo;
  - Il percorso su disco dell'immagine del post, se presente.
- Utilizzare il motore di templating Jinja per servire le pagine web (homepage e “Chi siamo”) mantenendo la struttura dell’HTML separata dai dati gestiti dall’applicazione. Occorre:
  - Creare le cartelle necessarie all’interno del progetto, inserendo i file HTML all’interno della cartella “templates”;
  - Modificare il file HTML sviluppato nei precedenti laboratori, eliminando i post statici e sostituendoli con le opportune espressioni e statement di programmazione. Nello stesso file, inserire un link verso la nuova pagina “Chi siamo” all’interno della navbar.
  - Adattare il file HTML per “Chi siamo” in modo da sfruttare le espressioni di Jinja per le immagini ed eventuali link.
