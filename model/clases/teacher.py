class teacher:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.lessons_list = []
        self.titles_less = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def lesson_append(self, lesson):
        self.lessons_list.append(lesson)

    def get_titles(self):
        res = f'Список предметов которые ведет преподаватель {self.get_name()}:\n'
        id = 0
        for tit in self.titles_less:
            res += f'{id}. {tit}\n'
            id += 1
        res += f'{id}. Выбрать все'
        return res

    def get_titles_lenght(self):
        return len(self.titles_less)

    def get_rasp(self):
        res = f'Расписание преподавателя {self.get_name()}:\n'
        for less in self.lessons_list:
            res += f'{less.__str__()}\n'
        return res

    def get_less_rasp(self, pred):
        res = f'Расписание предмета "{pred}":\n'
        for less in self.lessons_list:
            if less.get_title() == pred:
                res += f'{less.__str__()}\n'
        return res

    def get_titles_less(self):
        return self.titles_less

    def append_title(self, title):
        self.titles_less.append(title)

    def __str__(self):
        return f'id: {self.id}. ФИО: {self.name}'

    def parse_les_to_str(self):
        res = ''
        for less in self.titles_less:
            res += f'{less},'
        return res

    def get_info(self):
        return f'id: {self.id}, ФИО: {self.name}, ведет предметы: {self.parse_les_to_str()}'
