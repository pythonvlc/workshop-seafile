import os

class Gui:
    def __init__(self, api):
        self._api = api

    def run(self):
        self._build_api_map()
        menu_items = self._build_menu_items()
        self._menu = Menu("API options", menu_items)
        while True:
            choosen_option = self._menu.get_choosen_option()
            self._execute(choosen_option)

    def _build_api_map(self):
        self._functions = {}
        for i, function in enumerate(self._api.functions):
           self._functions[i] = function

    def _build_menu_items(self):
        menu_items = []
        [menu_items.append(MenuItem(index, function.name)) for index, function in self._functions.items()]
        return menu_items

    def _execute(self, option):
        response = self._functions[option].run()
        print(response)
        self._menu.wait_user_interaction()


class MenuItem:
    def __init__(self, index, name):
        self.index = index
        self.name = name


class Menu:
    def __init__(self, title, menu_items):
        self._title = title
        self._menu_items = menu_items
        self._blank_line = "\n"

    def get_choosen_option(self):
        try:
            self._show()
            choosen_option = int(input("Choose an option: "))
            menu_item = next((menu_item for menu_item in self._menu_items if menu_item.index == choosen_option), None)
            if menu_item is None:
                return self._try_again()
            return menu_item.index
        except ValueError:
            return self._try_again()
    
    def wait_user_interaction(self):
        input("Press any key to continue.")

    def _show(self):
        self._clear_screen()
        self._show_header()
        self._show_options()

    def _mismatch_option(self):
        print("Mismatch option.")
        self.wait_user_interaction()

    def _try_again(self):
        self._mismatch_option()        
        return self.get_choosen_option()

    def _clear_screen(self):
       os.system("clear") 

    def _show_header(self):
        print(self._title)
        print(self._blank_line)

    def _show_options(self):
        [print("{0} - {1}".format(menu_item.index, menu_item.name)) for menu_item in self._menu_items]
        print(self._blank_line)

