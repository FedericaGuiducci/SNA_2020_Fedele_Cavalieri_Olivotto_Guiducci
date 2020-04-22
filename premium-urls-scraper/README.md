# LinkedIn Free-account Users Url Scraper
Linkedin scraper per account free.
Permette di scaricare gli url di un tot di utenti settabile tramite il file config.ini

## Disclaimer
Scraping data off of LinkedIn is against their User Agreement. This is purely intended for educational purposes.

## Dependencies 
It is based on selenium 

## How to use
First, download the Chrome Driver from [here](http://chromedriver.chromium.org/) and extract it into the driver folder.

Set the number of users you want to scrape (2500 max) in the config.ini file.
Set your linkedin email and password in the config.ini file.

Finally, to scrape users run
```python3 main.py```

Il risultato in csv sarà posizionato nella directory export.

## Info sulla configurazione di parametri
E' supportata la multi configurazione di parametri e lo script scarica, per ogni configurazione, tutti i risultati avuti nella prima tab (max 2500).

Ogni configurazione è formata da 3 attributi: LOCATION, NEMPLOYEES, INDUSTRIES
Per ognuno degli attributi è possibile settarne una lista semplicemente separando con virgole.

Per creare una nuova configurazione c'è bisogno di dichiarare il seguente 
``` 
[FILTERCONFIG:X]
LOCATION = Y
NEMPLOYEES = Z,K
INDUSTRIES = J
```

IMPORTANTE! LA STRINGA 'FILTERCONFIG:' DEVE ESSERE PRESENTE. CAMBIARE SOLO L'INDICE.


Per il mapping delle key per ogni attributo dei filtri fare riferimento alle seguenti tabelle.

## N. employess filters
| Description       | KEY           |
| ----------------- | ------------- |
| 1 (Freelance)     | A             |
| 1 - 10            | B             |
| 11 - 50           | C             |
| 51 - 200          | D             |
| 201 - 500         | E             |
| 501 - 1000        | F             |
| 1001 - 5000       | G             |
| 5001 - 10000      | H             |
| more than 10000   | I             |

## Location geo filter
| Description   | KEY           |
| ------------- | ------------- |
| Italia        | 103350119     |
| Europa        | 100506914     |

## Industries filter 
| Settore                                                  | Numero settore |
|----------------------------------------------------------|----------------|
| Difesa e spazio                                          | 1              |
| VUOTO                                                    | 2              |
| Hardware                                                 | 3              |
| Software                                                 | 4              |
| Reti informatiche                                        | 5              |
| Internet                                                 | 6              |
| Semiconduttori                                           | 7              |
| Telecomunicazioni                                        | 8              |
| Studio legale                                            | 9              |
| Servizi legali                                           | 10             |
| Consulenza manageriale                                   | 11             |
| Biotecnologie                                            | 12             |
| Medicina                                                 | 13             |
| Strutture ospedaliere e sanità                           | 14             |
| Industria farmaceutica                                   | 15             |
| Veterinaria                                              | 16             |
| Strumenti medicali                                       | 17             |
| Cosmetica                                                | 18             |
| Accessori e moda                                         | 19             |
| Prodotti per lo sport                                    | 20             |
| Tabacco                                                  | 21             |
| Grande distribuzione                                     | 22             |
| Produzione di alimenti                                   | 23             |
| Elettronica di consumo                                   | 24             |
| Beni di consumo                                          | 25             |
| Arredamento                                              | 26             |
| Commercio al dettaglio                                   | 27             |
| Intrattenimento                                          | 28             |
| Gioco d'azzardo e casinò                                 | 29             |
| Tempo libero, viaggi e turismo                           | 30             |
| Alberghiero                                              | 31             |
| Ristorazione                                             | 32             |
| Sport                                                    | 33             |
| Alimenti e bevande                                       | 34             |
| Cinematografia e film                                    | 35             |
| Media radiotelevisivi                                    | 36             |
| Musei e istituzioni                                      | 37             |
| Belle arti                                               | 38             |
| Arti dello spettacolo                                    | 39             |
| Strutture e servizi per le attività ricreative           | 40             |
| Settore bancario                                         | 41             |
| Assicurazioni                                            | 42             |
| Servizi finanziari                                       | 43             |
| Immobiliare                                              | 44             |
| Investment banking                                       | 45             |
| Gestione investimenti                                    | 46             |
| Contabilità                                              | 47             |
| Edilizia                                                 | 48             |
| Materiali edili                                          | 49             |
| Architettura e progettazione                             | 50             |
| Ingegneria civile                                        | 51             |
| Aviazione e aerospazio                                   | 52             |
| Settore automobilistico                                  | 53             |
| Chimica                                                  | 54             |
| Macchinari industriali                                   | 55             |
| Minerario o minerali                                     | 56             |
| Petrolio ed energia                                      | 57             |
| Cantieri navali                                          | 58             |
| Servizi pubblici                                         | 59             |
| Tessile                                                  | 60             |
| Carta e prodotti forestali                               | 61             |
| Ferroviero                                               | 62             |
| Agricoltura                                              | 63             |
| Allevamento                                              | 64             |
| Lettiero caseario                                        | 65             |
| Settore pesca                                            | 66             |
| Istruzione primaria e secondaria                         | 67             |
| Istruzione superiore                                     | 68             |
| Gestione in ambito formativo                             | 69             |
| Ricerca                                                  | 70             |
| Militare                                                 | 71             |
| Ufficio legislativo                                      | 72             |
| Giudiziario                                              | 73             |
| Affari internaziomali                                    | 74             |
| Ammmistrazione governativo                               | 75             |
| Ufficio esecutivo                                        | 76             |
| Forze dell'ordine                                        | 77             |
| Pubblica sicurezza                                       | 78             |
| Politiche pubbliche                                      | 79             |
| Marketing e pubblicità                                   | 80             |
| Quotidiani                                               | 81             |
| Editoria                                                 | 82             |
| Stampa                                                   | 83             |
| Servizi informativi                                      | 84             |
| Biblioteche                                              | 85             |
| Servizi ambientali                                       | 86             |
| Corriere/spedizioni                                      | 87             |
| Servizi per la persona e la famiglia                     | 88             |
| Istituzioni religiose                                    | 89             |
| Organizazioni civiche e sociali                          | 90             |
| Beni primari                                             | 91             |
| Trasporti su strada/ferrovia                             | 92             |
| Magazzinaggio                                            | 93             |
| Linee aeree/Aviazione                                    | 94             |
| Marittimo                                                | 95             |
| Informatica e servizi                                    | 96             |
| Ricerche di mercato                                      | 97             |
| Pubbliche relazioni e comunicazioni                      | 98             |
| Desing                                                   | 99             |
| Gestione organizzazioni senza scopo di lucro             | 100            |
| Raccolta fondi                                           | 101            |
| Sviluppo di programmi                                    | 102            |
| Redazione e revione                                      | 103            |
| Selezione e ricerca di personale                         | 104            |
| Formazione professionale                                 | 105            |
| Capitale di rischio e private equity                     | 106            |
| Organizzazione politica                                  | 107            |
| Traduzione e localizzazione                              | 108            |
| Videogiochi                                              | 109            |
| Servizi per eventi                                       | 110            |
| Arti e mestieri                                          | 111            |
| Produzione elettrica ed elettronica                      | 112            |
| Media online                                             | 113            |
| Nanotecnologie                                           | 114            |
| Musica                                                   | 115            |
| Logistica e Supply Chain                                 | 116            |
| Plastica                                                 | 117            |
| Sicurezza informatica e delle reti                       | 118            |
| Wireless                                                 | 119            |
| ADR-Metodo alternativo di risoluzione delle controversie | 120            |
| Sicurezza e investigazioni                               | 121            |
| Servizi infrastrutturali                                 | 122            |
| Outsourcing/offshoring                                   | 123            |
| Salute, benessere e fitness                              | 124            |
| Medicina alternativa                                     | 125            |
| Produzione di media                                      | 126            |
| Animazione                                               | 127            |
| Immobili commerciali                                     | 128            |
| Mercati dei capitali                                     | 129            |
| Centri di ricerca                                        | 130            |
| Filantropia                                              | 131            |
| E-learning                                               | 132            |
| Vendite all'ingrosso                                     | 133            |
| Import-Export                                            | 134            |
| Ingegneria meccanica o industriale                       | 135            |
| Fotografia                                               | 136            |
| Risorse umane                                            | 137            |
| Forniture aziendali                                      | 138            |
| Servizi di salute mentale                                | 139            |
| Progettazione grafica                                    | 140            |
| Commercio internazionale e sviluppo                      | 141            |
| Vino e liquori                                           | 142            |
| Beni di lusso e gioielli                                 | 143            |
| Energia rinnovabile e ambiente                           | 144            |
| Vetro, ceramica e cemento                                | 145            |
| Imballaggi e contenitori                                 | 146            |
| Automazione industriale                                  | 147            |
| Relazioni (governo)                                      | 148            |