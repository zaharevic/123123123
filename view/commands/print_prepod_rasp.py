from view.commands.Command import command


class print_prepod_rasp(command):
    def get_description(self):
        return self.description

    def __init__(self, consoleUI):
        super().__init__(consoleUI)
        self.description = 'Вывести расписание предмета'

    def execute(self):
        self.consoleUI.print_prepod_rasp()
