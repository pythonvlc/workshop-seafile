import os


class MenuItem:
    def __init__(self, index, name, function):
        self.index = index
        self.name = name
        self.function = function


class Menu:
    def __init__(self, title, menu_items):
        self._title = title
        self._menu_items = menu_items
        self._blank_line = "\n"

    def get_choosen_action(self):
        try:
            self._show()
            choosen_option = int(input("Choose an option: "))
            menu_item = next((menu_item for menu_item in self._menu_items if menu_item.index == choosen_option), None)
            return menu_item.function
        except (ValueError, AttributeError):
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
        return self.get_choosen_action()

    def _clear_screen(self):
       os.system("clear") 

    def _show_header(self):
        print(self._title)
        print(self._blank_line)

    def _show_options(self):
        [print("{0} - {1}".format(menu_item.index, menu_item.name)) for menu_item in self._menu_items]
        print(self._blank_line)

