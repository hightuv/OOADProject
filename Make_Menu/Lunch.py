import random


class Lunch:
    def __init__(self, menu_categories, worksheet, dinner_history):
        self.worksheet = worksheet
        self.creation = 0
        self.check = 2
        self.lunch_history = []
        self.lunch_soup = []
        self.lunch_main = []
        self.lunch_sub = []
        self.lunch_side = []
        self.lunch_kimchi = ''
        self.menu_categories = menu_categories
        self.dinner_history = dinner_history

    def update_lunch_history(self):
        self.lunch_history = [self.lunch_soup, self.lunch_main, self.lunch_sub, self.lunch_side]

    def get_lunch_history(self):
        return self.lunch_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 13
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 점심 식단 선택 (국, 메인, 서브, 반찬)
            self.lunch_soup.append(random.choice(self.menu_categories[0]))
            self.lunch_main.append(random.choice(self.menu_categories[1]))
            self.lunch_sub.append(random.choice(self.menu_categories[2]))
            self.lunch_side.append(random.choice(self.menu_categories[3]))
            self.lunch_kimchi = random.choice(self.menu_categories[4])
            self.update_lunch_history()

            # 각 카테고리 별로 중복검사하면서 식단 생성 (국, 메인, 서브, 반찬)
            menu_category = 0
            while menu_category != len(self.get_lunch_history()):
                lunch_history = self.get_lunch_history()
                dinner_history = self.dinner_history
                check_trial_forward = 1
                check_trial_backward = 1
                check_forward = self.check
                check_backward = self.check
                flag = 1

                # 당일 저녁 식단 중복검사
                if lunch_history[menu_category][self.creation] == dinner_history[menu_category][self.creation]:
                    lunch_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                    self.update_lunch_history()
                    continue

                # 이전 점심, 저녁 식단과 중복검사
                while check_trial_backward <= check_backward:
                    if self.creation == 0:
                        break
                    elif self.creation < check_backward:
                        check_backward = self.creation

                    # 검사날짜 기준 이전에 저녁으로 나갈 메뉴인지 검사
                    if lunch_history[menu_category][self.creation] == dinner_history[menu_category][self.creation - check_trial_backward]:
                        lunch_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_lunch_history()
                        #초기화
                        flag = 0
                        break

                    # 검사날짜 기준 이전에 점심으로 나갈 메뉴인지 검사
                    elif lunch_history[menu_category][self.creation] == lunch_history[menu_category][self.creation - check_trial_backward]:
                        lunch_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_lunch_history()
                        # 초기화
                        flag = 0
                        break
                    check_trial_backward += 1

                if flag == 0:
                    # 처음부터 다시
                    continue

                # 이후 저녁 식단과 중복검사
                while check_trial_forward <= check_forward:
                    if self.creation + check_trial_forward >= len(dinner_history[menu_category]):
                        break

                    # 검사날짜 기준 이후에 저녁으로 나갈 메뉴인지 검사
                    if lunch_history[menu_category][self.creation] == dinner_history[menu_category][self.creation + check_trial_forward]:
                        lunch_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_lunch_history()
                        # 초기화
                        flag = 0
                        continue
                    check_trial_forward += 1

                if flag == 0:
                    # 처음부터 다시
                    continue

                # 워크시트에 반영
                self.worksheet[sheet_num][chr(col) + str(row)] = lunch_history[menu_category][self.creation]

                # 다음 카테고리로 넘어감
                menu_category += 1
                row += 1

            # 워크시트에 김치 입력
            self.worksheet[sheet_num][chr(col) + str(row)] = self.lunch_kimchi

            # 하루치 점심 식단 완성, creation을 1 증가
            self.creation += 1

            # 셀 포인터 이동
            row = 13
            col += 1

        # 최종 한 달치 lunch_history 갱신
        self.update_lunch_history()
