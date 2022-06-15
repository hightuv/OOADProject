import os
from datetime import datetime


class FileManager:

    def __init__(self, time):
        self.path = "./Menu/" + time
        self.menu_files = os.listdir(self.path)
        self.menu_categories = []
        self.menu_category_num = 0
        self.read_files()

        self.error = 0
        self.error_message = ''

    def read_files(self):
        now = datetime.now()
        try:
            for file_name in self.menu_files:
                f = open(self.path + '/' + file_name, 'r', encoding='utf-8')
                # print(file_name)
                tmp = f.read().split('\n')
                tmp = [t.strip() for t in tmp]
                self.menu_categories.append(tmp)
                f.close()
                self.menu_category_num += 1
        except IOError:
            self.error_message += now.strftime('%Y-%m-%d %H시 %M분 %S초에 ') + 'read_files() : IOError 발생'
            self.error += 1

    def get_menu_categories(self):
        return self.menu_categories

    def get_menu_category_num(self):
        return self.menu_category_num

    def get_error(self):
        return self.error

    def get_error_message(self):
        return self.error_message
