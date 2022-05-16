import os

class FileManager:

    def __init__(self, time):
        self.path = "./Menu/" + time
        self.menu_files = os.listdir(self.path)
        self.menu_categories = []
        self.menu_category_num = 0
        self.read_files()

    def read_files(self):
        for file_name in self.menu_files:
            f = open(self.path + '/' + file_name, 'r', encoding='utf-8')
            # print(file_name)
            tmp = f.read().split('\n')
            tmp = [t.strip() for t in tmp]
            self.menu_categories.append(tmp)
            f.close()
            self.menu_category_num += 1

    def get_menu_categories(self):
        return self.menu_categories

    def get_menu_category_num(self):
        return self.menu_category_num
