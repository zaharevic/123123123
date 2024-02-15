from view.Menu import main_menu
from presenter.presenter import presenter


class consoleUI:
    work = False
    menu = None

    def __init__(self):
        self.menu = main_menu(self)
        self.work = True

    @staticmethod
    def hello():
        print('Парсер сайта СамГТУ запускается!\nЗдравствуйте!')

    @staticmethod
    def print_answer(text):
        print(text)

    def print_menu(self):
        self.menu.print_menu()

    def start(self):
        self.hello()
        while self.work:
            self.print_menu()
            self.execute()

    @staticmethod
    def print_calendar():
        presenter.print_calendar()

    def execute(self):
        line = input()
        if self.check_text_for_int(line):
            num_command = int(line)
            if self.check_command(num_command):
                self.menu.execute(num_command)

    @staticmethod
    def check_text_for_int(text):
        if text.isdigit():
            return True
        else:
            return False

    def check_command(self, num_command):
        if num_command < (self.menu.get_size() + 1):
            return True
        else:
            return False


