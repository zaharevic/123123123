from view.commands.Command import command


class print_calendar(command):
    def get_description(self):
        return self.description

    def __init__(self, consoleUI):
        super(print_calendar, consoleUI).__init__()
        self.description = 'Print calendar'

    def execute(self):
        self.consoleUI.print_calendar()
