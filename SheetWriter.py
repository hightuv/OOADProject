import calendar
import openpyxl


class SheetWriter:
    def __init__(self, mi, wbm):
        self.workbook = wbm.get_workbook()
        self.worksheet = wbm.get_worksheet()
        self.year = mi.get_year()
        self.month = mi.get_month()
        self.first_week_served = mi.get_first_week_served()
        self.last_week_served = mi.get_last_week_served()
        self.img = 0
        self.img2 = 0
        self.num_of_sheet = 1
        self.set_num_of_sheet(self.year, self.month)

    def set_image(self):
        self.img = openpyxl.drawing.image.Image('./Image/로고1.png')
        self.img.height = 80
        self.img.width = 530
        self.img2 = openpyxl.drawing.image.Image('./Image/로고2.png')
        self.img2.height = 122
        self.img2.width = 270

    def get_num_of_sheet(self):
        return self.num_of_sheet

    def set_num_of_sheet(self, year, month):
        days = calendar.monthrange(year, month)[1]

        # 첫 주, 마지막 주를 제외한 나머지 주의 수를 구함
        days = days - self.first_week_served - self.last_week_served
        other_week = int(days / 7)

        # 생성할 전체 시트 수
        self.num_of_sheet = other_week
        if self.first_week_served > 0:
            self.num_of_sheet += 1
        if self.last_week_served > 0:
            self.num_of_sheet += 1

    def set_date(self):
        date = 1

        # 첫 번째 시트
        col = 72 - self.first_week_served + 1
        for i in range(self.first_week_served):
            self.worksheet[0][chr(col) + str(5)] = '%d/%d(%s)'%(self.month, date, self.get_weekday(self.year, self.month, date))
            date += 1
            col += 1

        # col 초기화
        col = 66 # B

        # 중간 시트
        for i in range(1, self.num_of_sheet - 1):
            for j in range(7):
                self.worksheet[i][chr(col) + str(5)] = '%d/%d(%s)'%(self.month, date, self.get_weekday(self.year, self.month, date))
                date += 1
                col += 1
            col = 66

        # col 초기화
        col = 66

        # 마지막 시트
        for i in range(self.last_week_served):

            self.worksheet[self.num_of_sheet - 1][chr(col) + str(5)] = '%d/%d(%s)' % (self.month, date, self.get_weekday(self.year, self.month, date))
            date += 1
            col += 1

    def get_weekday(self, year, month, date):
        day = calendar.weekday(year, month, date)
        if day == 0:
            return '월'
        elif day == 1:
            return '화'
        elif day == 2:
            return '수'
        elif day == 3:
            return '목'
        elif day == 4:
            return '금'
        elif day == 5:
            return '토'
        elif day == 6:
            return '일'

    def set_worksheet_name(self):
        # 첫 시트 이름
        date = 1
        month = self.month

        sheet_name = '%d.%d~' % (month, date)
        date += self.first_week_served - 1
        sheet_name += '%d.%d' % (month, date)
        date += 1
        self.set_image()
        self.worksheet[0].title = sheet_name
        self.worksheet[0].add_image(self.img, 'C2')
        self.worksheet[0].add_image(self.img2, 'G1')

        # 중간 시트 이름
        for i in range(1, self.num_of_sheet - 1):
            sheet_name = '%d.%d~' % (month, date)
            date += 6
            sheet_name += '%d.%d' % (month, date)
            date += 1
            self.worksheet.append(self.workbook.copy_worksheet(self.worksheet[0]))
            self.set_image()
            self.worksheet[i].title = sheet_name
            self.worksheet[i].add_image(self.img, 'C2')
            self.worksheet[i].add_image(self.img2, 'G1')

        # 마지막 시트 이름
        if self.last_week_served == 1:
            sheet_name = '%d.%d' % (month, date)
        else:
            sheet_name = '%d.%d~' % (month, date)
            date += self.last_week_served - 1
            sheet_name += '%d.%d'%(month, date)
            date += 1
        self.worksheet.append(self.workbook.copy_worksheet(self.worksheet[0]))
        self.set_image()
        self.worksheet[self.num_of_sheet - 1].title = sheet_name
        self.worksheet[self.num_of_sheet - 1].add_image(self.img, 'C2')
        self.worksheet[self.num_of_sheet - 1].add_image(self.img2, 'G1')


