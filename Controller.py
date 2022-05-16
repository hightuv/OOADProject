from MonthInvestigator import MonthInvestigator
from SheetCreator import SheetCreator
from FileManager import FileManager
from WorkBookManager import WorkBookManager
from Make_Menu.Dinner import Dinner
from Make_Menu.Lunch import Lunch
from Make_Menu.Breakfast import Breakfast
from Make_Menu.Snack import Snack
from Make_Menu.RiceAndPorridge import RiceAndPorridge
from Search import Search
from MenuManager import MenuManager
from Admin import Admin


class Controller:
    def __init__(self):
        self.monthInvestigator = 0
        self.workBookManager = 0

        # File Manager
        self.fm_dinner = 0
        self.fm_lunch = 0
        self.fm_breakfast = 0
        self.fm_snack = 0
        self.fm_riceandporridge = 0

        # Sheet Creator
        self.sheetCreator = 0

        # Menu Creator
        self.dinner = 0
        self.lunch = 0
        self.breakfast = 0
        self.snack = 0
        self.riceandporridge = 0

        # Searcher
        self.search = 0

        # Menu Manager
        self.menu_manager = 0

        # 알람에 출력할 결과
        self.result = 0

        # 관리자
        self.admin = Admin()

        
    def create_menu(self, year, month):
        self.monthInvestigator = MonthInvestigator(year, month)

        self.workBookManager = WorkBookManager(year, month)

        self.sheetCreator = SheetCreator(self.monthInvestigator, self.workBookManager)
        self.sheetCreator.set_worksheet_name()
        self.sheetCreator.set_date()

        self.fm_dinner = FileManager('Dinner')
        self.fm_lunch = FileManager('Lunch')
        self.fm_breakfast = FileManager('Breakfast')
        self.fm_snack = FileManager('Snack')
        self.fm_riceandporridge = FileManager('RiceAndPorridge')

        num_of_sheet = self.sheetCreator.get_num_of_sheet()
        first_week_served = self.monthInvestigator.get_first_week_served()
        last_week_served = self.monthInvestigator.get_last_week_served()

        # Dinner
        self.dinner = Dinner(self.fm_dinner.get_menu_categories(), self.workBookManager.get_worksheet())

        self.dinner.create_menu(0, first_week_served, 'first')
        for i in range(1, num_of_sheet - 1):
            self.dinner.create_menu(i, 7, 'middle')
        self.dinner.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Lunch
        self.lunch = Lunch(self.fm_lunch.get_menu_categories(), self.workBookManager.get_worksheet(), self.dinner.get_dinner_history())

        self.lunch.create_menu(0, first_week_served, 'first')
        for i in range(1, num_of_sheet - 1):
            self.lunch.create_menu(i, 7, 'middle')
        self.lunch.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Breakfast
        self.breakfast = Breakfast(self.fm_breakfast.get_menu_categories(), self.workBookManager.get_worksheet(), self.dinner.get_dinner_history(), self.lunch.get_lunch_history())

        self.breakfast.create_menu(0, first_week_served, 'first')
        for i in range(1, num_of_sheet - 1):
            self.breakfast.create_menu(i, 7, 'middle')
        self.breakfast.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Snack
        self.snack = Snack(self.fm_snack.get_menu_categories(), self.workBookManager.get_worksheet())
        self.snack.create_menu(0, first_week_served, 'first')
        for i in range(1, num_of_sheet - 1):
            self.snack.create_menu(i, 7, 'middle')
        self.snack.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Rice and Porridge
        self.riceandporridge = RiceAndPorridge(self.fm_riceandporridge.get_menu_categories(), self.workBookManager.get_worksheet())
        self.riceandporridge.create_menu(0, first_week_served, 'first')
        for i in range(1, num_of_sheet - 1):
            self.riceandporridge.create_menu(i, 7, 'middle')
        self.riceandporridge.create_menu(num_of_sheet - 1, last_week_served, 'last')

        self.workBookManager.save_workbook()
        self.result = self.workBookManager.get_result()

    def search_menu(self, year, month, search_menu):
        self.search = Search()
        self.search.do_search(year, month, search_menu)
        self.result = self.search.get_result()

    def call_menu_manager(self, meal, menu_category, manual, key):
        self.menu_manager = MenuManager()
        self.menu_manager.open_menu(meal, menu_category)
        if manual == 'search':
            self.menu_manager.search_menu(key)
        elif manual == 'add':
            self.menu_manager.add_menu(key)
        elif manual == 'delete':
            self.menu_manager.delete_menu(key)
        self.result = self.menu_manager.get_result()
        self.admin.update_error(self.menu_manager.get_error())

    def check_pass(self, password):
        self.admin.check_password(password)
        self.result = self.admin.get_result()

    def get_result(self):
        return self.result
'''

year = 2022
month = 4

mi = MonthInvestigator(year, month)

wbm = WorkBookManager(year, month)

sc = SheetCreator(mi, wbm)
sc.set_worksheet_name()
sc.set_date()

fm_dinner = FileManager('Dinner')
fm_lunch = FileManager('Lunch')
fm_breakfast = FileManager('Breakfast')
fm_snack = FileManager('Snack')
fm_riceandporridge = FileManager('RiceAndPorridge')

num_of_sheet = sc.get_num_of_sheet()
first_week_served = mi.get_first_week_served()
last_week_served = mi.get_last_week_served()

dinner = Dinner(fm_dinner.get_menu_categories(), wbm.get_worksheet())

dinner.create_menu(0, first_week_served, 'first')
for i in range(1, num_of_sheet - 1):
    dinner.create_menu(i, 7, 'middle')
dinner.create_menu(num_of_sheet - 1, last_week_served, 'last')
print('dinner끝')

lunch = Lunch(fm_lunch.get_menu_categories(), wbm.get_worksheet(), dinner.get_dinner_history())

lunch.create_menu(0, first_week_served, 'first')
for i in range(1, num_of_sheet - 1):
    lunch.create_menu(i, 7, 'middle')
lunch.create_menu(num_of_sheet - 1, last_week_served, 'last')

breakfast = Breakfast(fm_breakfast.get_menu_categories(), wbm.get_worksheet(), dinner.get_dinner_history(), lunch.get_lunch_history())
breakfast.create_menu(0, first_week_served, 'first')
for i in range(1, num_of_sheet - 1):
    breakfast.create_menu(i, 7, 'middle')
breakfast.create_menu(num_of_sheet - 1, last_week_served, 'last')

snack = Snack(fm_snack.get_menu_categories(), wbm.get_worksheet())
snack.create_menu(0, first_week_served, 'first')
for i in range(1, num_of_sheet - 1):
    snack.create_menu(i, 7, 'middle')
snack.create_menu(num_of_sheet - 1, last_week_served, 'last')

riceandporridge = RiceAndPorridge(fm_riceandporridge.get_menu_categories(), wbm.get_worksheet())
riceandporridge.create_menu(0, first_week_served, 'first')
for i in range(1, num_of_sheet - 1):
    riceandporridge.create_menu(i, 7, 'middle')
riceandporridge.create_menu(num_of_sheet - 1, last_week_served, 'last')

wbm.save_workbook()

search_year = 2022
search_month = 4
search = Search()
search.do_search(search_year, search_month, '소고기배추국')
result = search.get_result()
for r in result:
    print(r)

menu_manager = MenuManager()
menu_manager.open_menu('Lunch', '메인')
menu_manager.delete_menu('테스트메인1')
'''
