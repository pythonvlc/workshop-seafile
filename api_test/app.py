#!/usr/bin/env python3


import getpass
from model import Api, ListAccounts, CheckAccountInfo, CreateFooAccount, Exit, DeleteFooAccount
from view import Menu, MenuItem
from controller import Controller


class App:
    def run(self):
        self._model = self._build_model()
        view = self._build_view()
        Controller(view).run()

    def _build_model(self):
        user, password = self._get_user_password()
#        user, password = ("joansava@gmail.com", "sExt3rn08")
        api = Api.authenticate("http://seafileserver:8000/api2/", user, password) 
        api.add_functions([Exit(), ListAccounts(), CheckAccountInfo(), CreateFooAccount(), DeleteFooAccount()])
        return api

    def _get_user_password(self):
        user = input("admin user: ")
        password = getpass.getpass("admin password: ")
        return user, password

    def _build_view(self):
        menu_items = self._build_menu_items()
        menu = Menu("API options", menu_items)
        return menu

    def _build_menu_items(self):
        menu_items = []
        for i, function in enumerate(self._model.functions):
            menu_items.append(self._build_menu_item(i, function))
        return menu_items

    def _build_menu_item(self, index, function):
        menu_item = MenuItem(index, function.name, function)
        return menu_item


if __name__ == "__main__":
    App().run()
