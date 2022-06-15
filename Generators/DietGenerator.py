from Generators.DinnerGenerator import DinnerGenerator
from Generators.LunchGenerator import LunchGenerator
from Generators.BreakfastGenerator import BreakfastGenerator
from Generators.SnackGenerator import SnackGenerator
from Generators.RPGenerator import RPGenerator
from MonthInvestigator import MonthInvestigator
from WorkBookManager import WorkBookManager
from SheetWriter import SheetWriter
from FileManager import FileManager


class DietGenerator:
    def __init__(self, year, month):

        self.year = year
        self.month = month

        # Related to Excel
        self.monthInvestigator = MonthInvestigator(year, month)

        self.workBookManager = WorkBookManager(year, month)
        self.sheetWriter = SheetWriter(self.monthInvestigator, self.workBookManager)

        # File Managers
        self.fm_dinner = FileManager('Dinner')
        self.fm_lunch = FileManager('Lunch')
        self.fm_breakfast = FileManager('Breakfast')
        self.fm_snack = FileManager('Snack')
        self.fm_rp = FileManager('RiceAndPorridge')

        # Error Message
        self.error_message = ''

        # Count Errors
        self.error = 0

        # Diet Generators
        try:
            if self.fm_dinner.get_error() == 0 and self.workBookManager.get_error() == 0:
                self.dinnerGenerator = DinnerGenerator(self.fm_dinner.get_menu_categories(), self.workBookManager.get_worksheet())
            else:
                raise IOError('')
        except IOError:
            self.error += self.fm_dinner.get_error()
            self.error_message += self.fm_dinner.get_error_message()

        try:
            if self.fm_snack.get_error() == 0 and self.workBookManager.get_error() == 0:
                self.snackGenerator = SnackGenerator(self.fm_snack.get_menu_categories(), self.workBookManager.get_worksheet())
            else:
                raise IOError('')
        except IOError:
            self.error += self.fm_snack.get_error()
            self.error_message += self.fm_snack.get_error_message()

        try:
            if self.fm_rp.get_error() == 0 and self.workBookManager.get_error() == 0:
                self.rpGenerator = RPGenerator(self.fm_rp.get_menu_categories(), self.workBookManager.get_worksheet())
            else:
                raise IOError('')
        except IOError:
            self.error += self.fm_rp.get_error()
            self.error_message += self.fm_rp.get_error_message()

        self.lunchGenerator = None
        self.breakfastGenerator = None

        # Response
        self.response = None

    def generate_menu(self):
        self.sheetWriter.set_worksheet_name()
        self.sheetWriter.set_date()

        num_of_sheet = self.sheetWriter.get_num_of_sheet()
        first_week_served = self.monthInvestigator.get_first_week_served()
        last_week_served = self.monthInvestigator.get_last_week_served()

        # Generate Diet (Dinner)
        self.dinnerGenerator.create_menu(0, first_week_served, 'first')

        for i in range(1, num_of_sheet - 1):
            self.dinnerGenerator.create_menu(i, 7, 'middle')

        self.dinnerGenerator.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Generate Diet (Lunch)
        try:
            if self.fm_lunch.get_error() == 0 and self.workBookManager.get_error() == 0:
                self.lunchGenerator = LunchGenerator(self.fm_lunch.get_menu_categories(), self.workBookManager.get_worksheet(), self.dinnerGenerator.get_dinner_history())
            else:
                raise IOError('')
        except IOError:
            self.error += self.fm_lunch.get_error()
            self.error_message += self.fm_lunch.get_error_message()

        self.lunchGenerator.create_menu(0, first_week_served, 'first')

        for i in range(1, num_of_sheet - 1):
            self.lunchGenerator.create_menu(i, 7, 'middle')

        self.lunchGenerator.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Generate Diet (Breakfast)
        try:
            if self.fm_breakfast.get_error() == 0 and self.workBookManager.get_error() == 0:
                self.breakfastGenerator = BreakfastGenerator(self.fm_breakfast.get_menu_categories(), self.workBookManager.get_worksheet(), self.dinnerGenerator.get_dinner_history(), self.lunchGenerator.get_lunch_history())
            else:
                raise IOError('')
        except IOError:
            self.error += self.fm_breakfast.get_error()
            self.error_message += self.fm_breakfast.get_error_message()

        self.breakfastGenerator.create_menu(0, first_week_served, 'first')

        for i in range(1, num_of_sheet - 1):
            self.breakfastGenerator.create_menu(i, 7, 'middle')

        self.breakfastGenerator.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Generate Diet (Snack)
        self.snackGenerator.create_menu(0, first_week_served, 'first')

        for i in range(1, num_of_sheet - 1):
            self.snackGenerator.create_menu(i, 7, 'middle')

        self.snackGenerator.create_menu(num_of_sheet - 1, last_week_served, 'last')

        # Generate Diet (Rice and Porridge)
        self.rpGenerator.create_menu(0, first_week_served, 'first')

        for i in range(1, num_of_sheet - 1):
            self.rpGenerator.create_menu(i, 7, 'middle')

        self.rpGenerator.create_menu(num_of_sheet - 1, last_week_served, 'last')

        self.workBookManager.save_workbook()
        if self.workBookManager.get_error() == 0:
            self.response = '%d년 %d월 식단표가 생성되었습니다.' % (self.year, self.month)
        else:
            self.response = '%d년 %d월 식단표 생성 과정에 문제가 생겼습니다.' % (self.year, self.month)
            self.error += self.workBookManager.get_error()

    def get_response(self):
        return self.response

    def get_error(self):
        return self.error

    def get_error_message(self):
        return self.error_message
