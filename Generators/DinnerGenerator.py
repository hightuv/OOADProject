import random


class DinnerGenerator:
    def __init__(self, menu_categories, worksheet):
        self.worksheet = worksheet
        self.creation = 0
        self.check = 2
        self.dinner_history = []
        self.dinner_soup = []
        self.dinner_main = []
        self.dinner_sub = []
        self.dinner_side = []
        self.dinner_kimchi = ''
        self.menu_categories = menu_categories

    def update_dinner_history(self):
        self.dinner_history = [self.dinner_soup, self.dinner_main, self.dinner_sub, self.dinner_side]

    def get_dinner_history(self):
        return self.dinner_history

    def create_menu(self, sheet_num, serve_num, week_type):
        # 초기 셀 포인터
        row = 20
        if week_type == 'last':
            col = 66
        else:
            col = 72 - serve_num + 1

        for i in range(serve_num):
            # 저녁 식단 선택 (국, 메인, 서브, 반찬)
            self.dinner_soup.append(random.choice(self.menu_categories[0]))
            self.dinner_main.append(random.choice(self.menu_categories[1]))
            self.dinner_sub.append(random.choice(self.menu_categories[2]))
            self.dinner_side.append(random.choice(self.menu_categories[3]))
            self.dinner_kimchi = random.choice(self.menu_categories[4])
            self.update_dinner_history()

            # 각 카테고리 별로 중복검사하면서 식단 생성 (국, 메인, 서브, 반찬)
            menu_category = 0
            while menu_category != len(self.get_dinner_history()):
                dinner_history = self.get_dinner_history()
                check_trial_backward = 1
                check_backward = self.check
                flag = 1
                # 처음 생성하는 저녁 식단은 중복검사 안함

                # 두 번째로 생성하는 저녁 식단부터 중복검사 수행
                # 기준 날짜로부터 check_trial만큼 떨어진 곳의 저녁 식단과 비교하여 중복검사 진행
                while check_trial_backward <= check_backward:
                    # check 값보다 생성된 식단이 적으면 check을 self.creation의 값과 같게 함
                    # 예를 들어, check가 2인데, self.creation이 1이면 check을 1로 하여 하루 전까지만 검사하도록 함
                    if self.creation == 0:
                        break
                    elif self.creation < check_backward:
                        check_backward = self.creation
                    
                    # 생성한 저녁 식단 기준으로 check_trial만큼의 이전 저녁 식단과 비교
                    if dinner_history[menu_category][self.creation] == dinner_history[menu_category][self.creation - check_trial_backward]:
                        dinner_history[menu_category][self.creation] = random.choice(self.menu_categories[menu_category])
                        self.update_dinner_history()
                        # 초기화
                        continue

                    # 중복 검사에서 문제가 없으면 수행하게 됨
                    check_trial_backward += 1

                # 워크시트에 반영
                self.worksheet[sheet_num][chr(col) + str(row)] = dinner_history[menu_category][self.creation]
                
                # 다음 카테고리로 넘어감
                menu_category += 1
                row += 1

            # 워크시트에 김치 반영
            self.worksheet[sheet_num][chr(col) + str(row)] = self.dinner_kimchi
            
            # 하루치 저녁 식단 완성, creation을 1 증가
            self.creation += 1

            # 셀 포인터 이동
            row = 20
            col += 1
        
        # 최종 한 달치 dinner_history 갱신
        self.update_dinner_history()
