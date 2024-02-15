from view.commands.print_calendar import print_calendar


class main_menu:
    command_list = None

    def __init__(self, consoleUI):
        self.command_list = []
        self.command_list.append(print_calendar(consoleUI))

    def print_menu(self):
        result = ''
        for i in range(len(self.command_list)):
            result += f'{i + 1}. {self.command_list[i].get_description()}\n'
        print(result)

    def get_size(self):
        return len(self.command_list)

    def execute(self, number):
        self.command_list[number - 1].execute()
