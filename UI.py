import sys
from Controller import Controller
from PyQt5.QtWidgets import *


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.controller = Controller()
        self.setWindowTitle('식단표 관리 프로그램')
        self.resize(800, 350)

        # 식단표 생성 / 검색 그룹박스
        groupbox_make_search = QGroupBox('식단표 생성 / 검색')

        # 식단표 생성 / 검색 수평박스 구성요소
        year_label = QLabel('연도 : ', self)
        year_spinbox = QSpinBox(self)
        year_spinbox.setRange(0, 9999)
        year_spinbox.setValue(2022)
        month_label = QLabel('월 :', self)
        month_spinbox = QSpinBox(self)
        month_spinbox.setRange(1, 12)
        search_menu_label = QLabel('검색할 메뉴 이름 : ', self)
        search_menu_lineedit = QLineEdit(self)

        makemenu_button = QPushButton('생성', self)
        makemenu_button.clicked.connect(lambda: self.controller.create_menu(year_spinbox.value(), month_spinbox.value()))
        makemenu_button.clicked.connect(lambda: message.setText(self.controller.get_result()))

        search_button = QPushButton('검색', self)
        search_button.clicked.connect(lambda: self.controller.search_menu(year_spinbox.value(), month_spinbox.value(), search_menu_lineedit.text()))
        search_button.clicked.connect(lambda: message.setText(self.controller.get_result()))

        # 수평박스에 라벨, 입력라인, 버튼 삽입
        hbox_make_search = QHBoxLayout()
        hbox_make_search.addStretch(1)
        hbox_make_search.addWidget(year_label)
        hbox_make_search.addWidget(year_spinbox)
        hbox_make_search.addWidget(month_label)
        hbox_make_search.addWidget(month_spinbox)
        hbox_make_search.addWidget(search_menu_label)
        hbox_make_search.addWidget(search_menu_lineedit)
        hbox_make_search.addWidget(makemenu_button)
        hbox_make_search.addWidget(search_button)
        hbox_make_search.addStretch(1)

        # 그룹박스에 위에서 만든 수평박스 삽입
        groupbox_make_search.setLayout(hbox_make_search)

        # 메뉴 추가 / 삭제 그룹박스
        groupbox_editmenu = QGroupBox('메뉴 추가 / 삭제')

        # 메뉴 추가 / 삭제 수평박스 구성요소
        meal_label = QLabel('식사 종류 :', self)
        select_meal = QComboBox(self)
        select_meal.addItem('아침')
        select_meal.addItem('점심')
        select_meal.addItem('저녁')
        select_meal.addItem('간식')
        select_meal.addItem('밥/죽')
        

        category_label = QLabel('카테고리 : ', self)
        select_category = QComboBox(self)
        select_category.addItem('밥')
        select_category.addItem('죽')
        select_category.addItem('국')
        select_category.addItem('메인')
        select_category.addItem('서브')
        select_category.addItem('반찬')
        select_category.addItem('김치')
        select_category.addItem('간식')

        menu_label = QLabel('메뉴 이름 :', self)
        menu_lineedit = QLineEdit(self)

        search_button = QPushButton('검색', self)
        search_button.clicked.connect(lambda: self.controller.call_menu_manager(select_meal.currentText(), select_category.currentText(), 'search', menu_lineedit.text()))
        search_button.clicked.connect(lambda: message.setText(self.controller.get_result()))
        add_button = QPushButton('추가', self)
        add_button.clicked.connect(lambda: self.controller.call_menu_manager(select_meal.currentText(), select_category.currentText(), 'add', menu_lineedit.text()))
        add_button.clicked.connect(lambda: message.setText(self.controller.get_result()))
        delete_button = QPushButton('삭제', self)
        delete_button.clicked.connect(lambda: self.controller.call_menu_manager(select_meal.currentText(), select_category.currentText(), 'delete', menu_lineedit.text()))
        delete_button.clicked.connect(lambda: message.setText(self.controller.get_result()))

        # 수평박스에 구성요소 삽입
        hbox_editmenu = QHBoxLayout()
        hbox_editmenu.addStretch(1)
        hbox_editmenu.addWidget(meal_label)
        hbox_editmenu.addWidget(select_meal)
        hbox_editmenu.addWidget(category_label)
        hbox_editmenu.addWidget(select_category)
        hbox_editmenu.addWidget(menu_label)
        hbox_editmenu.addWidget(menu_lineedit)
        hbox_editmenu.addWidget(search_button)
        hbox_editmenu.addWidget(add_button)
        hbox_editmenu.addWidget(delete_button)
        hbox_editmenu.addStretch(1)

        # 그룹박스에 위에서 만든 수평박스 삽입
        groupbox_editmenu.setLayout(hbox_editmenu)

        # 알림 그룹박스
        groupbox_message = QGroupBox('알림')
        message = QTextEdit()
        vbox_message = QVBoxLayout()
        vbox_message.addWidget(message)
        groupbox_message.setLayout(vbox_message)

        # 관리자 그룹박스
        groupbox_admin = QGroupBox('관리자 모드 진입')
        pass_label = QLabel('Password : ')
        pass_lineedit = QLineEdit()
        pass_lineedit.setEchoMode(QLineEdit.Password)
        login_button = QPushButton('로그인', self)
        login_button.clicked.connect(lambda: self.controller.check_pass(pass_lineedit.text()))
        login_button.clicked.connect(lambda: message.setText(self.controller.get_result()))
        vbox_admin = QVBoxLayout()
        vbox_admin.addWidget(pass_label)
        vbox_admin.addWidget(pass_lineedit)
        vbox_admin.addWidget(login_button)
        groupbox_admin.setLayout(vbox_admin)

        grid = QGridLayout()

        grid.addWidget(groupbox_make_search, 0, 0)
        grid.addWidget(groupbox_editmenu, 1, 0)
        grid.addWidget(groupbox_message, 2, 0)
        grid.addWidget(groupbox_admin, 3, 0)
        self.setLayout(grid)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
