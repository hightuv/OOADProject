from DietSearcher import DietSearcher
from Generators.DietGenerator import DietGenerator
from MenuManager import MenuManager
from Admin import Admin
from ErrorCollector import ErrorCollector


class Controller:
    def __init__(self):
        # DietGenerator
        self.dietGenerator = None

        # Searcher
        self.searcher = None

        # Menu Manager
        self.menu_manager = None

        # 관리자
        self.admin = Admin()

        # 알람에 출력할 결과
        self.response = None

        # ErrorCollector
        self.errorCollector = ErrorCollector()

    def generate_menu(self, year, month):
        self.dietGenerator = DietGenerator(year, month)

        if self.dietGenerator.get_error() == 0:
            self.dietGenerator.generate_menu()
        else:
            self.update_error_log(self.dietGenerator.get_error_message())
            return

        if self.dietGenerator.get_error() == 0:
            self.response = self.dietGenerator.get_response()
        else:
            self.update_error_log(self.dietGenerator.get_error_message())
            return

    def search_diet(self, year, month, menu_name):
        self.searcher = DietSearcher()
        self.searcher.search(year, month, menu_name)

        if self.searcher.get_error() != 0:
            self.update_error_log(self.searcher.get_error_message())
        self.response = self.searcher.get_response()

    def call_menu_manager(self, meal, menu_category, manual, key):
        self.menu_manager = MenuManager()
        self.menu_manager.open_menu(meal, menu_category)
        if manual == 'search':
            self.menu_manager.search_menu(key)
        elif manual == 'add':
            self.menu_manager.add_menu(key)
        elif manual == 'delete':
            self.menu_manager.delete_menu(key)

        if self.menu_manager.get_error() != 0:
            self.update_error_log(self.menu_manager.error_message())

        self.response = self.menu_manager.get_response()

    def update_error_log(self, message):
        self.errorCollector.logging(message)

    def try_login(self, password):
        self.admin.check_password(password)
        if self.admin.get_error() != 0:
            self.update_error_log(self.admin.get_error_message())
        self.response = self.admin.get_response()

    def get_response(self):
        return self.response

