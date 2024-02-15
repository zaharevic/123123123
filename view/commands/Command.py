from abc import abstractmethod


class command:
    description = None
    consoleUI = None

    @classmethod
    @abstractmethod
    def __init__(cls, consoleUI):
        cls.consoleUI = consoleUI

    @classmethod
    @abstractmethod
    def get_description(cls):
        return cls.description

    @classmethod
    @abstractmethod
    def execute(cls):
        pass
