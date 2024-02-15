class lesson:
    def __init__(self, name, start, end, teacher_name):
        self.name = name
        self.start = start
        self.end = end
        self.teacher_name = teacher_name

    def get_name(self):
        return self.name

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_teachers_name(self):
        return self.teacher_name

    def set_name(self, name):
        try:
            self.name = name
            return True
        except:
            return False

    def set_teacher_name(self, name):
        try:
            self.teacher_name = name
            return True
        except:
            return False

    def set_start(self, start):
        try:
            self.start = start
            return True
        except:
            return False

    def set_end(self, end):
        try:
            self.end = end
            return True
        except:
            return False

    def __str__(self) -> str:
        return f'title: {self.name};\nteacher name: {self.teacher_name};\nstart: {self.start};\nend: {self.end};\n'
