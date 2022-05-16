import random

class Snack:
    def __init__(self, menu_categories, worksheet):
        self.worksheet = worksheet
        self.snack_tmp1 = 'snack1'
        self.snack_tmp2 = 'snack2'
        self.snack = 'snack'
        self.menu_categories = menu_categories

    def get_snack_tmp1(self):
        return self.snack_tmp1

    def get_snack_tmp2(self):
        return self.snack_tmp2

    def get_snack(self):
        return self.snack

    def get_snack_history(self):
        snack_history = [self.snack_tmp1, self.snack_tmp2, self.snack]
        return snack_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 18
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 저녁 식단 선택
            self.snack = random.choice(self.menu_categories[0])

            # 간식 중복검수
            while (self.snack == self.snack_tmp1) or (self.snack == self.snack_tmp2):
                self.snack = random.choice(self.menu_categories[0])
            # 간식 입력
            self.worksheet[sheet_num][chr(col) + str(row)] = self.snack

            # 2일간은 겹치는 메뉴가 나오지 않도록 하는 장치
            self.snack_tmp1 = self.snack_tmp2
            self.snack_tmp2 = self.snack

            # 셀 포인터 이동
            row = 18
            col += 1
