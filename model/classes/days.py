class days:
    lessons_list = None

    def __init__(self):
        self.lessons_list = []

    def add(self, lesson):
        self.lessons_list.append(lesson)

    def __str__(self):
        res = ''
        for i in range(len(self.lessons_list)):
            res += self.lessons_list[i].__str__()
            res += '\n'
        return res
