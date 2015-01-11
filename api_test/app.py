#!/usr/bin/env python3

import os
import sys
import requests
import getpass

class Api():
    @classmethod
    def authenticate(Api, api_url, user, password):
        auth_url = "{0}auth-token/".format(api_url)
        payload = {"username": user, "password": password}
        r = requests.post(auth_url, data=payload)
        token = r.json()["token"]
        return Api(api_url, token)

    def __init__(self, api_url, token):
        self._api_url = api_url
        self._authorization_token = {"Authorization": "Token {0}".format(token)}
        self._json_formatted = {"Accept": "application/json; indent=4"} 

    def add_functions(self, functions):
        self.functions = functions
        for function in self.functions:
            function.api_url = self._api_url
            function.authorization_token = self._authorization_token
            function.json_formatted = self._json_formatted

class ListAccounts:
    def __init__(self):
        self.name = "List accounts"

    def run(self):
        list_accounts_url = "{0}accounts/".format(self.api_url)
        headers = dict(list(self.authorization_token.items()) + list(self.json_formatted.items()))
        payload = {"start": "-1", "limit": "-1", "scope": "DB"}
        r = requests.get(list_accounts_url, headers=headers, data=payload)
        return r.json()

class CheckAccountInfo:
    def __init__(self):
        self.name = "Check account info"

    def run(self):
        check_account_info_url = "{0}account/info/".format(self.api_url)
        headers = dict(list(self.authorization_token.items()) + list(self.json_formatted.items()))
        r = requests.get(check_account_info_url, headers=headers)
        return r.json()

class Exit:
    def __init__(self):
        self.name = "Exit"

    def run(self):
        sys.exit(0)

class Gui:
    def __init__(self, api):
        self._blank_line = "\n"
        self._api = api

    def run(self):
        self._build_api_map()
        while True:
            self._show_menu()
            option = self._get_menu_option()
            self._execute(option)

    def _build_api_map(self):
        self._functions = {}
        for i, function in enumerate(self._api.functions):
           self._functions[i] = function

    def _show_menu(self):
        self._clear_screen()
        self._show_header()
        self._show_options()

    def _clear_screen(self):
       os.system("clear") 

    def _show_header(self):
        print("API options")
        print(self._blank_line)

    def _show_options(self):
        for k, v in self._functions.items():
            print("{0} - {1}".format(k, v.name))
        print(self._blank_line)

    def _get_menu_option(self):
        return int(input("Choose an option: "))

    def _execute(self, option):
        try:
            response = self._functions[option].run()
            print(response)
            self._wait_user_interaction()
        except KeyError:
            self._mismatch_option()

    def _wait_user_interaction(self):
        input("Press any key to continue.")

    def _mismatch_option(self):
        print("Mismatch option.")
        self._wait_user_interaction()

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
