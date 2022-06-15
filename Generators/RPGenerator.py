import random


class RPGenerator:
    def __init__(self, menu_categories, worksheet):
        self.worksheet = worksheet
        self.rice_porridge_tmp1 = ['rice1', 'porridge1']
        self.rice_porridge_tmp2 = ['rice2', 'porridge2']
        self.rice_porridge = ['rice', 'porridge']
        self.menu_categories = menu_categories

    def get_rice_porridge_tmp1(self):
        return self.rice_porridge_tmp1

    def get_rice_porridge_tmp2(self):
        return self.rice_porridge_tmp2

    def get_rice_porridge(self):
        return self.rice_porridge

    def get_rice_porridge_history(self):
        rice_porridge_history = [self.rice_porridge_tmp1, self.rice_porridge_tmp2, self.rice_porridge]
        return rice_porridge_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = [6, 12, 19]

        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 밥, 죽 선택
            self.rice_porridge[0] = random.choice(self.menu_categories[0])
            self.rice_porridge[1] = random.choice(self.menu_categories[1])

            # 죽 중복검수
            while (self.rice_porridge[1] == self.rice_porridge_tmp1[1]) or (self.rice_porridge[1] == self.rice_porridge_tmp2[1]):
                self.rice_porridge[1] = random.choice(self.menu_categories[1])
            for r in row:
                # 밥/죽 입력
                self.worksheet[sheet_num][chr(col) + str(r)] = self.rice_porridge[0] + '/' + self.rice_porridge[1]

            # 2일간은 겹치는 메뉴가 나오지 않도록 하는 장치
            self.rice_porridge_tmp1 = self.rice_porridge_tmp2.copy()
            self.rice_porridge_tmp2 = self.rice_porridge.copy()

            # 셀 포인터 이동
            col += 1
