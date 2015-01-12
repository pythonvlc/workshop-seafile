import sys
import requests


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
