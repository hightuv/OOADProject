

class MenuManager:
    def __init__(self):
        self.menu_category = './Menu'
        self.menu = []
        self.filename = ''
        self.result = ''
        self.error = 0

    def open_menu(self, meal, menu_category):
        # 경로 파악
        if meal in ['아침', '점심', '저녁']:
            if meal == '아침':
                self.menu_category += '/Breakfast'
            if meal == '점심':
                self.menu_category += '/Lunch'
            elif meal == '저녁':
                self.menu_category += '/Dinner'
            if menu_category == '국':
                self.menu_category += '/03_국.txt'
            elif menu_category == '메인':
                self.menu_category += '/04_메인.txt'
            elif menu_category == '서브':
                self.menu_category += '/05_서브.txt'
            elif menu_category == '반찬':
                self.menu_category += '/06_반찬.txt'

        elif meal == '밥/죽':
            self.menu_category += '/RiceAndPorridge'
            if menu_category == '밥':
                self.menu_category += '/01_밥.txt'
            elif menu_category == '죽':
                self.menu_category += '/02_죽.txt'

        elif meal == '간식':
            self.menu_category += '/Snack'
            if menu_category == '간식':
                self.menu_category += '/01_간식.txt'
        
        # 경로 확정
        self.filename = self.menu_category

        # 파일 열기
        f = open(self.filename, 'r', encoding='utf-8')

        # 메뉴 파악
        menu_tmp = f.readlines()
        for m in menu_tmp:
            m = m.strip()
            self.menu.append(m)
        f.close()

    def search_menu(self, menu_name):
        if menu_name not in self.menu:
            self.result = menu_name +'은 존재하지 않는 메뉴입니다.'
            return -1
        else:
            self.result = menu_name + '은 존재하는 메뉴입니다.'
            return 0
        
    def add_menu(self, new_menu):
        # 존재하지 않는 메뉴이면
        if self.search_menu(new_menu) == -1:
            self.menu.append(new_menu)
            # 파일 열기
            f = open(self.filename, 'a', encoding='utf-8')
            # 쓰기
            f.write('\n' + new_menu)
            # 파일 닫기
            f.close()
            self.result = new_menu + ' 추가완료.'
        else:
            self.result = new_menu + '은(는) 이미 존재합니다.'
            self.error += 1

    def delete_menu(self, delete_menu):
        # 존재하는 메뉴이면
        if self.search_menu(delete_menu) == 0:
            self.menu.remove(delete_menu)
            # 파일 열기
            f = open(self.filename, 'w', encoding='utf-8')
            # 쓰기
            for i in range(len(self.menu)):
                f.write(self.menu[i])
                if i != len(self.menu) - 1:
                    f.write('\n')
            # 파일 닫기
            f.close()
            self.result = delete_menu + ' 삭제완료'
        else:
            self.result = delete_menu + '은(는) 존재하지 않습니다.'
            self.error += 1

    def get_error(self):
        return self.error

    def get_result(self):
        return self.result
