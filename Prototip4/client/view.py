from User import User
from DaoUserClient import DaoUserClient


class ViewConsole:

    def __init__(self):
        self.daoClient = DaoUserClient()
        self.token = ""
        self.logged = False
        self.selected_child = None
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Taps")
        print("5: Quit")
        while True:
            option = input("Enter Option: ")
            if not option.isdigit():
                print("ERROR: You must enter a number between 1 and 5")
                continue
            optionInt = int(option)
            if optionInt < 1 or optionInt > 5:
                print("ERROR: Option must be between 1 and 5")
                continue
            return optionInt
        
    def viewGeneral(self):
        while True:
            option = self.viewShowMenu()
            if option == 1:
                self.viewLogin()
            elif option == 2:
                self.viewLoginToken(self.token)
            elif option == 3:
                if not self.logged:
                    print("You must login first (option 1 or 2)")
                    continue
                self.viewChilds(self.token)
            elif option == 4:
                if not self.logged:
                    print("You must login first (option 1 or 2)")
                    continue
                if not self.selected_child:
                    print("You must select a child first (option 3)")
                    continue
                self.viewTaps(self.token)
            elif option == 5:
                print("Bye!")
                break


    def viewChilds(self, token: str):
        childs = self.daoClient.childToken(token)
        if not childs:
            print("No childs or error")
            return
        print("CHILDS:")
        for c in childs:
            print("ID:", c.get('id'), "CHILD:", c.get('username') or c.get('name') or 'unknown')
        child_id = input("Select Child ID: ")
        found = False
        for c in childs:
            if str(c.get('id')) == child_id:
                self.selected_child = c
                found = True
                break
        if found:
            print("Child selected:", self.selected_child)
        else:
            print("Child does not exist")
            self.selected_child = None

    def viewLoginToken(self, token: str):
        print("View LOGIN TOKEN")
        resposta_user = self.daoClient.loginToken(token)
        if resposta_user:
            self.viewUser(resposta_user)
            self.token = resposta_user.token
            self.logged = True
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        username = input("Username o email: ")
        passwd = input("Password: ")
        user = User(None, username, passwd, None, None, None)
        resposta_user = self.daoClient.login(user)
        if resposta_user:
            self.viewUser(resposta_user)
            self.token = resposta_user.token
            self.logged = True
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self, user: User):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")
    
    def viewTaps(self, token: str):
        if not self.selected_child:
            print("You must select a child first (option 3)")
            return
        child_id = self.selected_child.get('id')
        print("Showing taps for:", self.selected_child)
        taps = self.daoClient.taps(token, child_id)
        if taps:
            print("TAPS:")
            for t in taps:
                print(t)
        else:
            print("No taps found")


if __name__ == '__main__':
    viewConsole = ViewConsole()
    viewConsole.viewGeneral()
