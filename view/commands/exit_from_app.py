from view.commands.Command import command


class exit_from_app(command):
    def get_description(self):
        return self.description

    def __init__(self, consoleUI):
        super().__init__(consoleUI)
        self.description = 'Выход'

    def execute(self):
        self.consoleUI.exit()
