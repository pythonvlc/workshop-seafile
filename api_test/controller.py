import os

class Controller:
    def __init__(self, view):
        self._view = view

    def run(self):
        while True:
            action = self._view.get_choosen_action()
            self._execute(action)

    def _execute(self, action):
        response = action.run()
        print(response)
        self._view.wait_user_interaction()

