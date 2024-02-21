
class lesson:
    def __init__(self, title, start, end, teachers, lesson_type):
        self.title = title
        self.start = start
        self.end = end
        self.teachers = teachers
        self.lesson_type = lesson_type

    def get_title(self):
        return self.title

    def get_start(self):
        return self.start

    def get_lesson_type(self):
        return self.lesson_type

    def get_teachers_names_str(self):
        res = ''
        for t in self.teachers:
            res += t.get_name()
            res += ', '
        return res

    def __str__(self) -> str:
        return f'Название предмета: {self.title};\n' \
               f'Тип пары: {self.lesson_type};\n' \
               f'Имена преподавателей: {self.get_teachers_names_str()};\n' \
               f'Начало пары: {self.start};\n' \
               f'Конец пары: {self.end};\n'

    def str_for_saving(self):
        return f'title: {self.title};\n' \
               f'lesson type: {self.lesson_type};\n' \
               f'teachers names: {self.get_teachers_names_str()};\n' \
               f'start: {self.start};\n' \
               f'end: {self.end};\n'
