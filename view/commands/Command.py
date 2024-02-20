from abc import abstractmethod


class command:
    description = None
    consoleUI = None

    def __init__(cls, consoleUI):
        cls.consoleUI = consoleUI

    def get_description(cls):
        return cls.description
