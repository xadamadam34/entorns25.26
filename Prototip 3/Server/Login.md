Caso de Uso: Login (Inicio de sesión)
Descripción

El usuario introduce sus credenciales para autenticarse en el sistema y obtener acceso a funcionalidades protegidas mediante un token.

Actores

Usuario, Cliente, Servidor, Base de Datos (BBDD)

Precondiciones
El usuario está registrado en el sistema
El sistema está operativo
El cliente puede comunicarse con el servidor
Postcondiciones
El usuario queda autenticado
Se genera un token válido
El token se almacena para futuras peticiones
Secuencia Normal
#	Acción (actor)	Reacción (sistema)
1	Usuario introduce usuario y contraseña	El cliente captura las credenciales
2	Cliente envía petición de login	Servidor recibe la solicitud
3	—	El servidor valida credenciales
4	—	El servidor consulta usuario en la BBDD
5	—	La BBDD devuelve datos del usuario
6	—	El servidor verifica credenciales
7	—	Genera token de autenticación
8	—	Guarda el token en la BBDD
9	—	Envía token al cliente
10	Usuario queda autenticado	Fin del caso de uso
Alternativas:
Si las credenciales son incorrectas → acceso denegado
Si el usuario no existe → mensaje de usuario no registrado
Si hay fallo de conexión → error de red
Excepciones:
#	Situación	Reacción del sistema
p	Sin conexión del usuario	No se puede enviar la petición
q	Error del servidor	Mensaje de error interno
⏱ Rendimiento

El sistema debe completar el login en menos de 2 segundos

Frecuencia

Aproximadamente 100 veces al día

Importancia:

Vital

Urgencia:

Inmediata

Comentarios:
Es requisito para acceder a cualquier funcionalidad protegida,
Se recomienda hash de contraseñas,
El token debe tener expiración
