from view.commands.Command import command


class print_pred_info(command):
    def get_description(self):
        return self.description

    def __init__(self, consoleUI):
        super().__init__(consoleUI)
        self.description = 'Вывести расписание преподавателя'

    def execute(self):
        self.consoleUI.print_pred_info()
