import requests

from Prototip.Server import ViewConsole

class User:
    def __init__(self, username, nom, password, email, rol="tutor"):
        self.username = username
        self.nom = nom
        self.password = password
        self.email = email
        self.rol = rol

    def __str__(self):
        return self.nom


class daoUserClient:
    def getUserByUsername(self, username):
        # peticion Http al webService (request)
        response = requests.get("http://localhost:5000/user?username=" + username)

        # si la peticion ok code response == 200
        if response.status_code == 200:
            # obtener json
            user_data_raw = response.json()
            # print("type", type(user_data_raw))

            # crear objecte User si lo hay encontrado
            if 'msg' in user_data_raw.keys():
                return None
            # si no se ha encontrado devuelve none
            else:
                user = User(
                    user_data_raw['username'],
                    user_data_raw['nom'],
                    user_data_raw['password'],
                    user_data_raw['email'],
                    user_data_raw['rol']
                )
                return user

        return None
    
    class ViewConsole:
        @staticmethod
        def getInputUsername():
            username = input("Introduce el nombre de usuario: ")
            user = dao.getUserByUsername(username)
            return user

    @staticmethod
    def showUserInfo(user):
        if user is None:
            print("❌ Usuario no encontrado")
        else:
            print("✅ Usuario encontrado:")
            print(f"Username: {user.username}")
            print(f"Nombre: {user.nom}")
            print(f"Email: {user.email}")
            print(f"Rol: {user.rol}")

if __name__ == "__main__":
    dao = daoUserClient()
    username = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(user)

    



''''
class ViewConsole:
    def getInputUsername():
        # TOdo
        return None

    def showUserInfo(username):
        # to-do
        return None


daoUserClient = daoUserClient()
u = daoUserClient.getUserByUsername("rob")
print(u)

u = daoUserClient.getUserByUsername("Not exist")
print(u)
'''