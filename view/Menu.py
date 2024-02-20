from view.commands.print_calendar import print_calendar
from view.commands.print_prepod_rasp import print_prepod_rasp
from view.commands.exit_from_app import exit_from_app
from view.commands.edit_filtres import edit_filtres
from view.commands.print_pred_info import print_pred_info


class main_menu:
    command_list = None

    def __init__(self, consoleUI):
        self.command_list = []
        self.command_list.append(print_calendar(consoleUI))
        self.command_list.append(print_prepod_rasp(consoleUI))
        self.command_list.append(print_pred_info(consoleUI))
        self.command_list.append(edit_filtres(consoleUI))
        self.command_list.append(exit_from_app(consoleUI))

    def print_menu(self):
        result = '\nМеню парсера СамГТУ:\n'
        for i in range(len(self.command_list)):
            result += f'{i + 1}. {self.command_list[i].get_description()}\n'
        print(result)

    def get_size(self):
        return len(self.command_list)

    def execute(self, number):
        self.command_list[number - 1].execute()
