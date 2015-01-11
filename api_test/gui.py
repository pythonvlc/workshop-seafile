import os

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
