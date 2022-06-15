import random


class Lunch:
    def __init__(self, menu_categories, worksheet, dinner_history):
        self.worksheet = worksheet
        self.lunch_tmp1 = ['l_soup1', 'l_main1', 'l_sub1', 'l_side1', 'l_kimchi1']
        self.lunch_tmp2 = ['l_soup2', 'l_main2', 'l_sub2', 'l_side2', 'l_kimchi2']
        self.lunch = ['l_soup', 'l_main', 'l_sub', 'l_side', 'l_kimchi']
        self.menu_categories = menu_categories
        self.dinner_history = dinner_history

    def get_lunch_tmp1(self):
        return self.lunch_tmp1

    def get_lunch_tmp2(self):
        return self.lunch_tmp2

    def get_lunch(self):
        return self.lunch

    def get_lunch_history(self):
        lunch_history = [self.lunch_tmp1, self.lunch_tmp2, self.lunch]
        return lunch_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 13
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 점심 식단 선택
            self.lunch[0] = random.choice(self.menu_categories[0])
            self.lunch[1] = random.choice(self.menu_categories[1])
            self.lunch[2] = random.choice(self.menu_categories[2])
            self.lunch[3] = random.choice(self.menu_categories[3])
            self.lunch[4] = random.choice(self.menu_categories[4])

            # 이틀 안에 나왔던 식단인지 검수 (국, 메인, 서브, 반찬) *저녁 식단도 확인
            for j in range(0, len(self.lunch) - 1):
                while (self.lunch[j] == self.lunch_tmp1[j])\
                        or (self.lunch[j] == self.lunch_tmp2[j])\
                        or (self.lunch[j] == self.dinner_history[0][j])\
                        or (self.lunch[j] == self.dinner_history[1][j])\
                        or (self.lunch[j] == self.dinner_history[2][j]):
                    self.lunch[j] = random.choice(self.menu_categories[j])
                self.worksheet[sheet_num][chr(col) + str(row)] = self.lunch[j]
                row += 1

            # 김치 입력
            self.worksheet[sheet_num][chr(col) + str(row)] = self.lunch[4]

            # 2일간은 겹치는 메뉴가 나오지 않도록 하는 장치
            self.lunch_tmp1 = self.lunch_tmp2.copy()
            self.lunch_tmp2 = self.lunch.copy()

            # 셀 포인터 이동
            row = 13
            col += 1