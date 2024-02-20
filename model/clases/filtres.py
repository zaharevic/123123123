class filtres:

    def __init__(self):
        self.is_lec = 1
        self.is_prac = 1
        self.is_lab = 1

    def switch_lab(self):
        if self.is_lab == 1:
            self.is_lab = 0
        elif self.is_lab == 0:
            self.is_lab = 1

    def switch_prac(self):
        if self.is_prac == 1:
            self.is_prac = 0
        elif self.is_prac == 0:
            self.is_prac = 1

    def switch_lec(self):
        if self.is_lec == 1:
            self.is_lec = 0
        elif self.is_lec == 0:
            self.is_lec = 1

    def meaning_to_str(self, mean):
        if mean == 1:
            return 'Вкл'
        elif mean == 0:
            return 'Выкл'

    def get_types_arr(self):
        res = []
        if self.is_lab:
            res.append('Лабораторные работы')
        if self.is_lec:
            res.append('Лекции')
        if self.is_prac:
            res.append('Практические занятия')
        return res



    def __str__(self):
        return f'Показывать:\n' \
               f'1. Лекции: {self.meaning_to_str(self.is_lec)}\n' \
               f'2. Практические занятия: {self.meaning_to_str(self.is_prac)}\n' \
               f'3. Лабараторные работы: {self.meaning_to_str(self.is_lab)}\n' \
               f'4. Выход\n'
