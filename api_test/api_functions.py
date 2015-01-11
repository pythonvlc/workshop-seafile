import sys
import requests

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
