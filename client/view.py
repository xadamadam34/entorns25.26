from User import *
from DaoUserClient import *

class ViewConsole:

    daoClient=DaoUserClient()
    token=""
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit):
                optionInt=int(option)
                if(optionInt >0 and optionInt <3):
                    return optionInt
            
            print("Error: Introdueix una opció correcta")

        
    def viewGeneral(self):
        option=-1
        while(option!=2):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                case 2:
                    #login Token
                    self.viewLoginToken(self.token)
                case 3:
                    #Childs
                    print("Childs")
                    #self.viewLogin()
                case 4:
                    # Quit
                    print("Adeu, Gràcies per utilitzar l'aplicació")

    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user=self.daoClient.loginToken(token)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")


viewConsole=ViewConsole()

viewConsole.viewGeneral()
 




