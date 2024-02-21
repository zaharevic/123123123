from view.Menu import main_menu
from presenter.presenter import presenter


class consoleUI:
    work = False
    menu = None
    pres = None

    def __init__(self):
        self.menu = main_menu(self)
        self.work = True
        self.pres = presenter()

    @staticmethod
    def hello():
        print('Парсер сайта СамГТУ запускается...\nЗдравствуйте! Парсер запущен\n')

    def print_menu(self):
        self.menu.print_menu()

    def start(self):
        self.hello()
        self.signing()
        self.pres.start()
        while self.work:
            self.print_menu()
            self.execute()

    def phpsesid_sigining(self):
        phpsessid = input('Введите phpsessid:\n')
        return self.pres.phpsessid_signing(phpsessid)

    def signing(self):
        work1 = True

        while work1:
            if self.phpsesid_sigining():
                print('\nВы успешно вошли!')
                work1 = False
            else:
                print('Вы ввели неверные данные!')

    def print_calendar(self):
        flag1 = True
        flag2 = True

        while flag1:
            st_date = input('Введите дату с которой выводить расписание(в формате гггг-мм-дд):')
            end_date = input('Введите дату до которой выводить расписание(в формате гггг-мм-дд):')
            if self.pres.try_parse_str_to_datatime(st_date, end_date):
                print(self.pres.get_calendar(st_date, end_date))
                flag1 = False
            else:
                print("Введена неверная дата!")
        while flag2:
            try:
                answer = int(input(
                    'Вы хотите сохранить файл?\n'
                    '1.Да, сохранить в .xlsx\n'
                    '2.Да, сохранить в .json\n'
                    '3.Не сохранять\n'))
                if answer == 1:
                    path = input('\nВведите путь, в который сохранить файл или введите 0 для сохранения в приложении:')
                    print('\nФайл успешно сохранен\n')
                    self.pres.save_to_excel(path)
                    flag2 = False
                elif answer == 2:
                    path = input('\nВведите путь, в который сохранить файл или введите 0 для сохранения в приложении:')
                    self.pres.save_to_json(path)
                    print('\nФайл успешно сохранен\n')
                    flag2 = False
                elif answer == 3:
                    flag2 = False
                else:
                    print('Вы ввели неверные данные')
            except Exception as e:
                print(f'Ошибка сохранения! Попробуйте снова! {e}')

    def print_prepod_rasp(self):
        flag1 = True
        flag2 = True

        print(self.pres.get_prep_list())
        while flag1:
            try:
                answer = int(input('Введите Id нужного преподавателя: '))
                if self.pres.prep_is_real(answer):
                    while flag2:
                        print(self.pres.get_prep_titles(answer))
                        ans = int(input('Введите id нужного предмета: '))
                        if ans < self.pres.get_title_lenght(answer):
                            print(self.pres.get_less_resp(answer, ans))
                            flag2 = False
                        elif ans == self.pres.get_title_lenght(answer):
                            print(self.pres.get_prep_rasp(answer))
                            flag2 = False
                        elif ans == self.pres.get_title_lenght(answer) + 1:
                            flag2 = False
                        else:
                            print('Неверные данные!')
                    flag1 = False
                else:
                    print("Вы ввели неверные данные!")
            except Exception as e:
                print(f'Error! {e}')

    def execute(self):
        line = input()
        if self.check_text_for_int(line):
            num_command = int(line)
            if self.check_command(num_command):
                self.menu.execute(num_command)

    @staticmethod
    def check_text_for_int(text):
        if text.isdigit():
            return True
        else:
            return False

    def check_command(self, num_command):
        if num_command < (self.menu.get_size() + 1):
            return True
        else:
            return False

    def exit(self):
        self.work = False
        print("Пока!")

    def edit_filtres(self):
        flag = True

        while flag:
            print(self.pres.print_filtres())
            answer = input('Введите номер фильтра который необходимо изменить: ')
            if answer in ['1', '2', '3']:
                self.pres.switch_filtres(answer)
                print('Изменения были успешно приняты!\n')
            elif answer == '4':
                flag = False
            else:
                print('Неверные данные\n')

    def print_pred_info(self):
        flag1 = True

        while flag1:
            try:
                print(self.pres.get_unique_less())
                ans = int(input('Введите id нужного предмета: '))
                if self.pres.check_pred_id(ans):
                    print(self.pres.get_prep_info(ans))
                    print(self.pres.print_less_rasp(ans))
                    flag1 = False
                else:
                    print('Введены неверные данные!')
            except Exception as e:
                print(f'Ошибка! {e}')
