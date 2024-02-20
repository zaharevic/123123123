class teachers_list:
    def __init__(self):
        self.teachers_list = []

    def get_teachers_list(self):
        return self.teachers_list

    def append_teacher(self, teach):
        self.teachers_list.append(teach)

    def get_lenght(self):
        return len(self.teachers_list)

    def teacher_is_unique(self, name):
        for t in self.teachers_list:
            if t.get_name() == name:
                return False
        return True

    def get_teacher_by_id(self, id_pr):
        for t in self.teachers_list:
            if t.get_id() == id_pr:
                return t
        return None

    def get_teacher_by_name(self, name):
        for t in self.teachers_list:
            if t.get_name() == name:
                return t
        return None

    def __str__(self):
        res = ''
        res += 'Список преподователей:\n'
        for teach in self.teachers_list:
            res += f'{teach.__str__()}\n'
        return res
