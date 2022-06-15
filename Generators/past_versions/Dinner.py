import random

class Dinner:
    def __init__(self, menu_categories, worksheet):
        self.worksheet = worksheet
        self.dinner_tmp1 = ['d_soup1', 'd_main1', 'd_sub1', 'd_side1', 'd_kimchi1']
        self.dinner_tmp2 = ['d_soup2', 'd_main2', 'd_sub2', 'd_side2', 'd_kimchi2']
        self.dinner = ['d_soup', 'd_main', 'd_sub', 'd_side', 'd_kimchi']
        self.menu_categories = menu_categories

    def get_dinner_tmp1(self):
        return self.dinner_tmp1

    def get_dinner_tmp2(self):
        return self.dinner_tmp2

    def get_dinner(self):
        return self.dinner

    def get_dinner_history(self):
        dinner_history = [self.dinner_tmp1, self.dinner_tmp2, self.dinner]
        return dinner_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 20
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 저녁 식단 선택 (국, 메인, 서브, 반찬)
            self.dinner[0] = random.choice(self.menu_categories[0])
            self.dinner[1] = random.choice(self.menu_categories[1])
            self.dinner[2] = random.choice(self.menu_categories[2])
            self.dinner[3] = random.choice(self.menu_categories[3])
            self.dinner[4] = random.choice(self.menu_categories[4])

            # 이틀 안에 나왔던 식단인지 검수 (국, 메인, 서브, 반찬)
            for j in range(0, len(self.dinner) - 1):
                while (self.dinner[j] == self.dinner_tmp1[j]) or (self.dinner[j] == self.dinner_tmp2[j]):
                    self.dinner[j] = random.choice(self.menu_categories[j])
                self.worksheet[sheet_num][chr(col) + str(row)] = self.dinner[j]
                row += 1

            # 김치 입력
            self.worksheet[sheet_num][chr(col) + str(row)] = self.dinner[4]

            # 2일간은 겹치는 메뉴가 나오지 않도록 하는 장치
            self.dinner_tmp1 = self.dinner_tmp2.copy()
            self.dinner_tmp2 = self.dinner.copy()

            # 셀 포인터 이동
            row = 20
            col += 1
