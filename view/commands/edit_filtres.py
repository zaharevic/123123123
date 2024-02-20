from view.commands.Command import command


class edit_filtres(command):
    def get_description(self):
        return self.description

    def __init__(self, consoleUI):
        super().__init__(consoleUI)
        self.description = 'Изменить фильтры'

    def execute(self):
        self.consoleUI.edit_filtres()
