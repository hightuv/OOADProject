import calendar


class MonthInvestigator:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.first_day = self.get_first_day()
        self.last_day = self.get_last_day()
        self.first_week_served = 0
        self.last_week_served = 0
        self.set_first_week_served()
        self.set_last_week_served()

    def set_first_week_served(self):
        # 첫 주 Serve 횟수
        self.first_week_served = 7 - self.first_day

    def set_last_week_served(self):
        # 마지막 주 Serve 횟수
        self.last_week_served = self.last_day + 1

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_first_day(self):
        # 주어진 달 1일의 "요일"
        first_day = calendar.monthrange(self.year, self.month)[0]

        return first_day

    def get_last_day(self):
        last_day = 0
        # 다음 달 1일의 "요일"에서 1을 빼면 이번 달 마지막 날의 "요일"을 알 수 있다
        if self.month >= 12:
            last_day = calendar.monthrange(self.year + 1, (self.month + 1) - 12)[0]
        else:
            last_day = calendar.monthrange(self.year, self.month + 1)[0]

        # 주어진 달 마지막 날의 "요일"
        if last_day == 0:
            last_day = 6
        else:
            last_day -= 1

        return last_day

    def get_first_week_served(self):
        # 첫 주 Serve 횟수
        return self.first_week_served

    def get_last_week_served(self):
        # 마지막 주 Serve 횟수
        return self.last_week_served
