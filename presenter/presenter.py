from model.core import core


class presenter:
    model = None
    view = None

    def __init__(self):
        self.model = core()

    def get_calendar(self, st_d, end_d):
        return self.model.get_calendar(st_d, end_d)

    def phpsessid_signing(self, phpsessid):
        return self.model.phpsessid_signing(phpsessid)

    def start(self):
        self.model.start()

    def try_parse_str_to_datatime(self,str1,str2):
        return self.model.try_parse_str_to_datatime(str1, str2)

    def prep_is_real(self, id_pr):
        return self.model.prep_is_real(id_pr)

    def get_prep_rasp(self, pr_id):
        return self.model.get_prepod_rasp(pr_id)

    def get_prep_titles(self, pr_id):
        return self.model.get_prep_titles(pr_id)

    def print_filtres(self):
        return self.model.get_filtres()

    def switch_filtres(self, code):
        self.model.switch_filter(code)

    def get_prep_list(self):
        return self.model.get_prep_list()

    def get_less_resp(self, pr_id, l_id):
        return self.model.get_less_rasp(pr_id, l_id)

    def get_title_lenght(self, pr_id):
        return self.model.get_titles_lenght(pr_id)

    def save_to_excel(self, path):
        return self.model.parse_and_save_to_excel(path)

    def save_to_json(self, path):
        return self.model.parse_and_save_to_json(path)

    def get_prep_info(self, le_id):
        return self.model.get_prepod_info(le_id)

    def get_unique_less(self):
        return self.model.get_unique_less()

    def check_pred_id(self, id):
        return self.model.check_pred_id(id)

    def print_less_rasp(self, less_id):
        return self.model.print_less_rasp(less_id)
