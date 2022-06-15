import openpyxl


class WorkBookManager:
    def __init__(self, year, month):
        self.workbook = openpyxl.load_workbook('Format/포멧1.xlsx')
        self.worksheet = []
        self.worksheet.append(self.workbook.active)
        self.year = year
        self.month = month
        self.error = 0
        self.error_message = ''

    def get_workbook(self):
        return self.workbook

    def get_worksheet(self):
        return self.worksheet

    def save_workbook(self):
        # 최종 저장
        try:
            self.workbook.save('./Result/%d년 %d월 식단표.xlsx'%(self.year, self.month))
        except ValueError:
            self.error += 1
            self.error_message = '식단표 저장을 실패했습니다.'

    def get_error(self):
        return self.error

    def get_error_message(self):
        return self.error_message
