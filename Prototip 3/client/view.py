from User import *
from DaoUserClient import *

class ViewConsole:

    def __init__(self):
        self.daoClient = DaoUserClient()
        self.token = ""
        self.logged = False
        self.child_selected = False
        self.selected_child = None
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Taps")
        print("5: Quit")
        while(True):
            option=input("Enter Option: ")
            if not option.isdigit():
                print("ERROR: You must enter a number between 1 and 5")
                continue
            optionInt = int(option)
            if optionInt < 1 or optionInt > 5:
                print("ERROR: Option must be between 1 and 5")
                continue
            return optionInt
        
    def viewGeneral(self):
        option=-1
        while(True):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                    self.logged = True
                case 2:
                    #login Token
                    self.viewLoginToken(self.token)
                    self.logged = True
                case 3:
                    if not self.logged:
                        print("You must login first (option 1 or 2)")
                        continue
                    self.viewChilds(self.token)
                case 4: 
                    if not self.logged:
                        print("You must login first (option 1 or 2)")
                        continue
                    if not self.selected_child:
                        print("You must select a child first (option 3)")
                        continue
                    self.viewTaps(self.token)
                case 5:
                    # Quit
                    exit()
                    print("Bye!")


    def viewChilds(self, token):
        childs = self.daoClient.childToken(token)
        if not childs:
            print("No childs or error")
            return
        print("CHILDS:")
        for c in childs:
            print("ID:", c['id'], "CHILD:", c.get('username', c.get('name', 'unknown')))
        child_id = input("Select Child ID: ")
        found = False
        for c in childs:
            if str(c['id']) == child_id:
                self.selected_child = c
                found = True
                break
        if found:
            print("Child selected:", self.selected_child)
        else:
            print("Child does not exist")
            self.selected_child = None
            self.selected_child = True

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
    
    def viewTaps(self, token):
        if not self.selected_child:
            print("You must select a child first (option 3)")
            return
        
        child_id = self.selected_child['id']
        
        print("Showing taps for:", self.selected_child)
        taps = self.daoClient.taps(token, child_id)
        
        if taps:
            print("TAPS:")
            print(taps)
        else:
            print("No taps found")

viewConsole=ViewConsole()
selected_child = None
viewConsole.viewGeneral()
 




