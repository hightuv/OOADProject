import openpyxl


class WorkBookManager:
    def __init__(self, year, month):
        self.workbook = openpyxl.load_workbook('./Format/포멧1.xlsx')
        self.worksheet = []
        self.worksheet.append(self.workbook.active)
        self.year = year
        self.month = month
        self.result = ''

    def get_workbook(self):
        return self.workbook

    def get_worksheet(self):
        return self.worksheet

    def save_workbook(self):
        # 최종 저장
        self.workbook.save('./Result/%d년 %d월 식단표.xlsx'%(self.year, self.month))
        self.result = '%d년 %d월 식단표가 생성되었습니다.'%(self.year, self.month)

    def get_result(self):
        return self.result
