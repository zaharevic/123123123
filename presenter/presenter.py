#from view.ConsoleUI import consoleUI
from model.model import model


class presenter:
    @staticmethod
    def print_calendar():
        model.print_calendar()
        return True
