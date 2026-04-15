Caso de Uso: View Child (Cuidador / Tutor)
Descripción

El Cuidador o Tutor consulta la información del hijo en el sistema para visualizar sus datos.

Actores

Cuidador, Tutor, Cliente, Servidor, Base de Datos (BBDD)

Precondiciones
El usuario ha iniciado sesión correctamente
Tiene token válido
Tiene permisos de cuidador o tutor
Postcondiciones
Se muestran los datos del hijo
Secuencia Normal
#	Acción (actor)	Reacción (sistema)
1	Cuidador/Tutor solicita ver datos del hijo	El sistema recibe la solicitud
2	Cliente envía petición con token	Servidor recibe la petición
3	—	El sistema valida el token
4	—	El sistema verifica rol (cuidador/tutor)
5	—	Consulta datos del hijo en la BBDD
6	—	Devuelve datos al servidor
7	—	Envía datos al cliente
8	Usuario visualiza los datos	Fin del caso de uso
Alternativas: 
Si el token es inválido → se deniega acceso y se redirige a Login
Si no tiene permisos → error de autorización
Si no hay datos → mensaje “sin datos disponibles”
Excepciones: 
#	Situación	Reacción del sistema
p	Error de conexión	No se procesa la solicitud
q	Error del servidor	Mensaje de error interno
Rendimiento: 

El sistema debe responder en menos de 2 segundos

Frecuencia: 

Aproximadamente 80 veces al día

Importancia: 

Importante

Urgencia

Puede esperar

Comentarios
Depende del Login, 
Solo roles autorizados pueden acceder, 
Control de permisos obligatorio
