#!/usr/bin/env python3


import getpass
from api import Api
from api_functions import ListAccounts, CheckAccountInfo, Exit
from gui import Gui


def get_user_password():
    user = input("admin user: ")
    password = getpass.getpass("admin password: ")
    return user, password

def run():
#    user, password = get_user_password()
    user, password = ("joansava@gmail.com", "sExt3rn08")
    api = Api.authenticate("http://seafileserver:8000/api2/", user, password) 
    api.add_functions([Exit(), ListAccounts(), CheckAccountInfo()])
    gui = Gui(api)
    gui.run()

# que pasa si la autenticación no es correcta??
# que pasa si como opcion introduzco algo que no es convertible a integer??

if __name__ == "__main__":
    run()
