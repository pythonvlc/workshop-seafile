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
