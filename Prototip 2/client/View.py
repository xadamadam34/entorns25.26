from User import *
from DaoUserClient import *

class ViewConsole:

    daoClient = DaoUserClient()

    def viewShowmenu(self):
        print("1: Login")
        print("2: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit()):
                optionInt=int(option)
                if (optionInt > 0 and optionInt < 3):
                    return optionInt
               
            print("ERROR: Introduce un valor correcto")

    def viewGeneral(self):
        option=-1
        while(option!=2):
            option=self.viewShowmenu()
            match option:
                case 1:
                    self.viewLogin()
                    #login
                case 2:
                    #Quit
                    print("Saliendo de la aplicación...")

    def viewLogin(self):
        print("View LOGIN")
        print("Introduce el username/email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("",username, passwd, "", "", "")
        resposta_user = self.daoClient.login(user)

        if resposta_user:
            self.viewUser(resposta_user)
        else:
            self.viewUserNotAuthenticated()

    def viewUser(self,user):
        print("View User Authenticated")
        print(user)

    def viewUserNotAuthenticated(self):
        print("User NOT Authenticated")

viewConsole=ViewConsole()
viewConsole.viewGeneral()
