class days:
    lessons_list = None

    def __init__(self):
        self.lessons_list = []

    def add(self, lesson):
        self.lessons_list.append(lesson)

    def get_lesson_list(self):
        return self.lessons_list

    def get_teachers_name(self):
        result = []
        data = self.get_lesson_list()
        for lesson in data:
            names = lesson.get_teachers_name()
            for name in names:
                if name not in result:
                    result.append(name)
        return result

    def __str__(self):
        res = ''
        for i in range(len(self.lessons_list)):
            res += self.lessons_list[i].__str__()
            res += '\n'
        return res

    def str_for_save(self):
        res = ''
        for i in range(len(self.lessons_list)):
            res += self.lessons_list[i].str_for_saving()
            res += '\n'
        return res
