import random


class BreakfastGenerator:
    def __init__(self, menu_categories, worksheet, dinner_history, lunch_history):
        self.worksheet = worksheet
        self.creation = 0
        self.check = 2
        self.breakfast_history = []
        self.breakfast_soup = []
        self.breakfast_main = []
        self.breakfast_sub = []
        self.breakfast_side = []
        self.breakfast_kimchi = ''
        self.menu_categories = menu_categories
        self.dinner_history = dinner_history
        self.lunch_history = lunch_history

    def update_breakfast_history(self):
        self.breakfast_history = [self.breakfast_soup, self.breakfast_main, self.breakfast_sub, self.breakfast_side]

    def get_breakfast_history(self):
        return self.breakfast_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 7
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 점심 식단 선택 (국, 메인, 서브, 반찬)
            self.breakfast_soup.append(random.choice(self.menu_categories[0]))
            self.breakfast_main.append(random.choice(self.menu_categories[1]))
            self.breakfast_sub.append(random.choice(self.menu_categories[2]))
            self.breakfast_side.append(random.choice(self.menu_categories[3]))
            self.breakfast_kimchi = random.choice(self.menu_categories[4])
            self.update_breakfast_history()

            # 이틀 안에 나왔던 식단인지 검수 (국, 메인, 서브, 반찬)
            menu_category = 0
            while menu_category != len(self.get_breakfast_history()):
                breakfast_history = self.get_breakfast_history()
                lunch_history = self.lunch_history
                dinner_history = self.dinner_history
                check_trial_forward = 1
                check_trial_backward = 1
                check_forward = self.check
                check_backward = self.check
                flag = 1
                # 당일 저녁, 점심 식단 중복검사
                if breakfast_history[menu_category][self.creation] == dinner_history[menu_category][self.creation]:
                    breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                    self.update_breakfast_history()
                    continue
                
                elif breakfast_history[menu_category][self.creation] == lunch_history[menu_category][self.creation]:
                    breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                    self.update_breakfast_history()
                    continue

                # 이전 아침, 점심, 저녁 식단과 중복검사
                while check_trial_backward <= check_backward:
                    if self.creation == 0:
                        break
                    elif self.creation < check_backward:
                        check_backward = self.creation

                    # 검사날짜 기준 이전에 저녁으로 나갈 메뉴인지 검사
                    if breakfast_history[menu_category][self.creation] == dinner_history[menu_category][self.creation - check_trial_backward]:
                        breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_breakfast_history()
                        # 초기화
                        flag = 0
                        check_backward = self.check
                        break

                    # 검사날짜 기준 이전에 점심으로 나갈 메뉴인지 검사
                    elif breakfast_history[menu_category][self.creation] == lunch_history[menu_category][self.creation - check_trial_backward]:
                        breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_breakfast_history()
                        # 초기화
                        flag = 0
                        check_backward = self.check
                        break

                    # 검사날짜 기준 이전에 아침으로 나갈 메뉴인지 검사
                    elif breakfast_history[menu_category][self.creation] == breakfast_history[menu_category][self.creation - check_trial_backward]:
                        breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_breakfast_history()
                        # 초기화
                        flag = 0
                        check_backward = self.check
                        break

                    check_trial_backward += 1

                if flag == 0:
                    # 처음부터 다시
                    continue

                # 이후 점심, 저녁 식단과 중복검사
                while check_trial_forward <= check_forward:
                    # dinner_history[menu_category]와 lunch_history[menu_category]의 length는 동일하다
                    if self.creation + check_trial_forward == len(dinner_history[menu_category]):
                        break

                    # 검사날짜 기준 이후에 저녁으로 나갈 메뉴인지 검사
                    if breakfast_history[menu_category][self.creation] == dinner_history[menu_category][
                        self.creation + check_trial_forward]:
                        breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_breakfast_history()
                        # 초기화
                        flag = 0
                        check_backward = self.check
                        continue

                    # 검사날짜 기준 이후에 점심으로 나갈 메뉴인지 검사
                    elif breakfast_history[menu_category][self.creation] == lunch_history[menu_category][self.creation + check_trial_forward]:
                        breakfast_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_breakfast_history()
                        # 초기화
                        flag = 0
                        check_backward = self.check
                        continue
                    check_trial_forward += 1

                if flag == 0:
                    # 처음부터 다시
                    continue

                # 워크시트에 반영
                self.worksheet[sheet_num][chr(col) + str(row)] = breakfast_history[menu_category][self.creation]

                # 다음 카테고리로 넘어감
                menu_category += 1
                row += 1

            # 워크시트에 김치 입력
            self.worksheet[sheet_num][chr(col) + str(row)] = self.breakfast_kimchi

            # 하루치 점심 식단 완성, creation을 1 증가
            self.creation += 1

            # 셀 포인터 이동
            row = 7
            col += 1

        # 최종 한 달치 breakfast_history 갱신
        self.update_breakfast_history()
