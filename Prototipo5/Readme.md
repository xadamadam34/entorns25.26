# Projecte ENTORNS- ADAM i DANIAL - Reserva de Pistes Esportives

---

# 1 - Requisits Funcionals del Projecte

## Descripció:

L’aplicació permet als usuaris reservar pistes esportives (futbol, pàdel, bàsquet, etc.) des d’una plataforma web i mòbil. També permet als administradors gestionar pistes, horaris i reserves.

---

## Objectius del Projecte:

· Facilitar la reserva d’instal·lacions esportives.  
· Automatitzar la gestió de reserves.  
· Permetre la consulta d’horaris disponibles en temps real.  
· Gestionar usuaris i administradors de manera segura.  

---

## Actors de l’aplicació:

### Usuari:
· Registrar-se i iniciar sessió.  
· Consultar pistes disponibles.  
· Crear i cancel·lar reserves.  

### Administrador:
· Gestionar pistes esportives.  
· Gestionar usuaris.  
· Controlar totes les reserves.  

---

## Requisits Funcionals (RF)

· **RF1 – Registre i autenticació d’usuaris:** El sistema permet que els usuaris es registrin i iniciïn sessió amb correu i contrasenya.

· **RF2 – Gestió de reserves:** Els usuaris poden crear, consultar i cancel·lar reserves de pistes esportives.

---

## Requisits No Funcionals (RNF)

· **RNF1 – Seguretat:** Les contrasenyes s’emmagatzemen encriptades a la base de dades.

· **RNF2 – Rendiment:** L’aplicació respon a les peticions principals en menys de 2 segons.

---

---

# 2 - Requisits Tècnics de l’aplicació

## BackEnd:

El backend de l’aplicació es desenvolupa amb Python utilitzant el framework Flask per gestionar el servidor i les peticions HTTP.  
La comunicació entre el frontend i el backend es realitza mitjançant una API REST, utilitzant dades en format JSON.  
Per a la gestió de dades s’utilitza una base de dades MySQL, on s'emmagatzemen els usuaris, reserves i la resta d’informació necessària de l’aplicació.

---

## Tecnologies Backend:
· Python  
· Flask  
· API REST  
· JSON  
· MySQL  

---

## Funcionalitats Backend:
· Gestió d’usuaris  
· Registre i inici de sessió  
· Connexió amb MySQL  
· Validació de dades  
· Enviament i recepció de dades en format JSON  

---

## FrontEnd:

El frontend es desenvolupa amb tecnologies web bàsiques per crear una interfície intuïtiva i fàcil d’utilitzar.  
La comunicació amb el backend es fa mitjançant peticions HTTP a l’API REST desenvolupada amb Flask.

---

## Tecnologies Frontend:
· HTML  
· CSS  
· JavaScript  

---

## Funcionalitats Frontend:
· Formularis de registre i login  
· Visualització de dades  
· Interacció amb l’API REST  
· Interfície responsive i accessible  
