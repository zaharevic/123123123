from view.commands.Command import command


class print_calendar(command):
    def get_description(self):
        return self.description

    def __init__(self, consoleUI):
        super().__init__(consoleUI)
        self.description = 'Вывести расписание'

    def execute(self):
        self.consoleUI.print_calendar()
