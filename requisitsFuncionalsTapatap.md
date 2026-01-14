
# Requisits Funcionals tapatap


## Descripció del Projecte  

Ens adrecem a vostès des de l’Institut de Formació Professional Provençana de l’Hospitalet de Llobregat per presentar-los el projecte TapatApp. La idea d’aquest projecte neix de la necessitat d’una família de la nostra comunitat que va tenir un fill amb una malaltia visual rara anomenada cataracta congènita.
Una cataracta congènita és l'opacitat del cristal·lí de l'ull que està present en néixer. La incidència de cataracta congènita està al voltant dels 3 / 10.000 nens, a l'any de vida. A l'Hospital de Sant Joan de Déu s'han operat en l'últim any al voltant de 100 cataractes infantils.
Les cataractes són la causa més freqüent de ceguesa tractable en la infància i es podria fer una estimació de 200.000 nens cecs per cataracta al món.
L'ull amb cataracta congènita, un cop operat, ha de seguir un exhaustiu règim de rehabilitació per evitar l'ambliopia, el que coneixem comunament com "ull gandul", i aquí és on pretén ajudar TapatApp! 
A part del tractament amb lents de contacte d’alta graduació i, posteriorment, lents intraoculars, el tractament més eficaç possible en aquesta patologia consisteix en l’aplicació d’un pedaç (parche) a l’ull dominant, fent que l’ull operat es vegi forçat a desenvolupar-se el màxim possible. El repte en aquest sentit, és aconseguir que l’aplicació d’aquest tractament sigui el més equilibrada possible, per aconseguir el màxim desenvolupament d’aquest ull operat, sense penalitzar el de l’ull dominant, que també ha «d’aprendre a veure» en el que s’anomena l’etapa plàstica del cervell, que finalitza entre els 6-8 anys.
Durant aquesta etapa, el tractament amb pedaç varia en funció de l’edat de l’infant, començant per aplicar-lo la meitat del temps que estigui despert en els primers mesos de vida, i continuant amb un temps fix diari que estableix l’oftalmòleg. La dificultat real d’aquesta gestió rau en controlar el nombre de minuts que porta o li queda per portar al nen aquest pedaç, ja que el seu son acostuma a ser variable i molt freqüent durant al dia. Moltes famílies manifesten la dificultat de controlar això per les freqüents migdiades que fan els petits, i per la incertesa de quan s’adormiran en el que queda de dia.
L’objectiu de TapatApp consisteix en proporcionar a totes les famílies afectades per cataracta congènita, o qualsevol patologia que faci servir pedaç ocular, una eina senzilla i gratuïta que els ajudi a portar aquest tractament de la forma més equilibrada possible i, com a conseqüència, obtenir el màxim desenvolupament d’agudesa visual.
Esperant que el nostre projecte TapatApp, sigui del seu interès.








## Objectius

· Compartir informació amb el servei mèdic
· Control del temps del pegat de l'infant
· Accés restringit per tipus d'usuari al control del pegat. Aplicació Multiusuari.
· Control del tractament de la 1/2 del temps que l'infant està despert



## Actors de la App

Mare / cuidadora principal
Pare / cuidador principal
Cuidador secundari (avis, mestres, cangurs, monitors)
Mestre / educador infantil
Servei Mèdic
Administrador de l’associació
"Públic"



## Requisits Funcionals RF i Requisits No Funcionals

### RF: 
El sistema ha de registrar l’historial de temps d’ús del pedaç per dies. 
L’aplicació ha de notificar quan s’ha complert el temps diari indicat pel metge.
L’aplicació ha de permetre consultar informes o gràfiques d’evolució de l’ús del pedaç.
Ha de permetre configurar diferents horaris segons dies de la setmana.
Ha de permetre afegir notes o comentaris sobre cada sessió.
L’aplicació ha de ser accessible des de diversos dispositius (com a mínim mòbils).


### RNF: 
L’aplicació ha de ser senzilla i intuïtiva, pensada per a usuaris no tècnics (famílies).
L’aplicació ha de ser gratuïta per a tots els usuaris.
L’aplicació ha d’estar disponible en català i castellà, com a mínim.
El sistema ha de funcionar sense connexió a internet, almenys per les funcionalitats bàsiques (temporitzador i registre).


# Requisits Tècnics tapatpp

## 1. Backend (Servidor i Gestió de Dades)

El backend serà el cor del sistema, encarregat de gestionar dades, usuaris, i la lògica del sistema


### a. Requisits del Servidor 

- Allojament: Hosting compartit
- Base de dades: Mysql o MariaDB
- Sistema Operatiu: Linux o Windows
- WebService: Restful llibreria Python Flask

### b. Llenguatge de Programació


Python

### c.  Seguretat

- Autenticació i autorització pels usuaris
- Xifratge de dades HTTPS
- Còpies de seguretat automàtiques

## 2. Frontend 

### a. Tipus de Clients 


- App Mòbil: Android 
- Consola Python
- Framework Multiplataforma: Flutter (Apps IOS Android, Web, Desktop)

### b. Emmagazematge local i sincronització 

- Token, Nickname (Guardada localment)
- Seguretat: HTTPS, autenticació per token


### c. Gestió d'accessibilitat 

- Nivells A, AA, AAA d'acessibilitat


## 3. Requisits generals infraestructures

- Xarxa: Internet 
- Espai d'emmagatzematge a Servidor: 500 G.
- API a tercers: No em fem servir

### a. Gestió d'usuari i autenticació 

- Rols: Tutor i cuidador
- Seguretat password


### b. Requisits d'Infraestructura


- Xarxa: Internet 
- Espai d'emmagatzematge a Servidor: 500 G.
- API a tercers: No em fem servir

## 4. Requisits del Procés de Desenvolupament

- IDE: VScode Python, Android Studio
- Control de versions: git, Github
- Metodologia de desenvolupament: Scrum
- Testing i proves de qualitat(QA): Test i proves unitàries
