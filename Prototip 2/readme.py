# Entorns de desenvolupament 25-26

## Prototip 2

### Diagrama d'arquitectura

Pujar Diagrama d'arquitectura Client Server Prototip 2

### Diagrama de classes

Fer Diagrama de classes del **Server** (Mermaid)

WebService (Controlador), Dao's , ADT(Abstract data Class) User, Child, Tap ... 

**Client**

### End-Points

Definir els EndPoints necessaris per implementar el Prototip 2

#### Servei Login
End-point:  /login    
Method: POST  
Estat: Public  
Tipus petició : application/json  
Paramètres:  
- username : (string) username o email  
- password : (string)  password  

Resposta Usuari validat Ok:  
http Response Code: 200 ok  
```
{    
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "token12345",
    "idrole": "2",
    "msg": "Usuari Ok"
    "coderesponse": "1"
}
```

Resposta Usuari No validat: 
http Response Code: 400 ok
```
{
     "coderesponse": "0"
     "msg": "No validat"
}
```


#### Servei Login per Token 
End-point:  /login   
Method: POST  
Estat: Public  
Tipus petició :  application/json  
Paramètres Header: 'Authorization'   : (string) token   

Resposta Usuari validat Ok:  
http Response Code: 200 ok  
```
{
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "token12345",
    "idrole": "2",
    "msg": "Usuari Ok"
    "coderesponse": "1"
}
```

Resposta Usuari No validat:   
http Response Code: 400 ok  
```
{
    "coderesponse": "0"
     "msg": "No validat"
}
```


#### Servei Child
End-point:  /child    
Method: POST  
Estat: Privat (autenticació amb Token per Header)  
Tipus petició :  application/json  
Paramètres: iduser : (int) id_user  


Resposta No Child:  
```
{ 
   "msg": "1"
    "coderesponse": "1"

  [ ]
}
```

Resposta 1 Child:  
```
{ 
   "msg": "1"
    "coderesponse": "1"

  [ {
"id": 1,
    "child_name": "Carol Child",
    "sleep_average": 8,
    "treatment_id": 1,
    "time": 6

}]
}
```

Resposta Varis Child:  
```
{ 
   "msg": "2"
    "coderesponse": "1"

  [ {
"id": 1,
    "child_name": "Carol Child",
    "sleep_average": 8,
    "treatment_id": 1,
    "time": 6

},
{
    "id": 2,
    "child_name": "Jaco Child",
    "sleep_average": 10,
    "treatment_id": 2,
    "time": 6
}
]
}
```

