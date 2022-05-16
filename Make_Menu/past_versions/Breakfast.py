import random


class Breakfast:
    def __init__(self, menu_categories, worksheet, dinner_history, lunch_history):
        self.worksheet = worksheet
        self.breakfast_tmp1 = ['b_soup1', 'b_main1', 'b_sub1', 'b_side1', 'b_kimchi1']
        self.breakfast_tmp2 = ['b_soup2', 'b_main2', 'b_sub2', 'b_side2', 'b_kimchi2']
        self.breakfast = ['b_soup', 'b_main', 'b_sub', 'b_side', 'b_kimchi']
        self.menu_categories = menu_categories
        self.dinner_history = dinner_history
        self.lunch_history = lunch_history

    def get_breakfast_tmp1(self):
        return self.breakfast_tmp1

    def get_breakfast_tmp2(self):
        return self.breakfast_tmp2

    def get_breakfast(self):
        return self.breakfast

    def get_breakfast_history(self):
        breakfast_history = [self.breakfast_tmp1, self.breakfast_tmp2, self.breakfast]
        return breakfast_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 7
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 아침 식단 선택
            self.breakfast[0] = random.choice(self.menu_categories[0])
            self.breakfast[1] = random.choice(self.menu_categories[1])
            self.breakfast[2] = random.choice(self.menu_categories[2])
            self.breakfast[3] = random.choice(self.menu_categories[3])
            self.breakfast[4] = random.choice(self.menu_categories[4])

            # 이틀 안에 나왔던 식단인지 검수 (국, 메인, 서브, 반찬) *저녁, 점심 식단도 확인
            for j in range(0, len(self.breakfast) - 1):
                while (self.breakfast[j] == self.breakfast_tmp1[j])\
                        or (self.breakfast[j] == self.breakfast_tmp2[j])\
                        or (self.breakfast[j] == self.dinner_history[0][j])\
                        or (self.breakfast[j] == self.dinner_history[1][j])\
                        or (self.breakfast[j] == self.dinner_history[2][j])\
                        or (self.breakfast[j] == self.lunch_history[0][j])\
                        or (self.breakfast[j] == self.lunch_history[1][j])\
                        or (self.breakfast[j] == self.lunch_history[2][j]):
                    self.breakfast[j] = random.choice(self.menu_categories[j])
                self.worksheet[sheet_num][chr(col) + str(row)] = self.breakfast[j]
                row += 1

            # 김치 입력
            self.worksheet[sheet_num][chr(col) + str(row)] = self.breakfast[4]

            # 2일간은 겹치는 메뉴가 나오지 않도록 하는 장치
            self.breakfast_tmp1 = self.breakfast_tmp2.copy()
            self.breakfast_tmp2 = self.breakfast.copy()

            # 셀 포인터 이동
            row = 7
            col += 1
