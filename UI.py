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
        search_diet_label = QLabel('검색할 메뉴 이름 : ', self)
        search_diet_lineedit = QLineEdit(self)

        makemenu_button = QPushButton('생성', self)
        makemenu_button.clicked.connect(lambda: self.controller.generate_menu(year_spinbox.value(), month_spinbox.value()))
        makemenu_button.clicked.connect(lambda: message.setText(self.controller.get_response()))

        search_button = QPushButton('검색', self)
        search_button.clicked.connect(lambda: self.controller.search_diet(year_spinbox.value(), month_spinbox.value(), search_diet_lineedit.text()))
        search_button.clicked.connect(lambda: message.setText(self.controller.get_response()))

        # 수평박스에 라벨, 입력라인, 버튼 삽입
        hbox_make_search = QHBoxLayout()
        hbox_make_search.addStretch(1)
        hbox_make_search.addWidget(year_label)
        hbox_make_search.addWidget(year_spinbox)
        hbox_make_search.addWidget(month_label)
        hbox_make_search.addWidget(month_spinbox)
        hbox_make_search.addWidget(search_diet_label)
        hbox_make_search.addWidget(search_diet_lineedit)
        hbox_make_search.addWidget(makemenu_button)
        hbox_make_search.addWidget(search_button)
        hbox_make_search.addStretch(1)

        # 그룹박스에 위에서 만든 수평박스 삽입
        groupbox_make_search.setLayout(hbox_make_search)

        # 메뉴 추가 / 삭제 (아침~저녁) 그룹박스
        groupbox_editmenu_time = QGroupBox('메뉴 추가 / 삭제 (아침~저녁)')

        # 메뉴 추가 / 삭제 (아침~저녁) 수평박스 구성요소
        meal_label = QLabel('식사 시간대 :', self)
        select_time = QComboBox(self)
        select_time.addItem('아침')
        select_time.addItem('점심')
        select_time.addItem('저녁')

        category_label = QLabel('카테고리 : ', self)
        select_category = QComboBox(self)
        select_category.addItem('메인')
        select_category.addItem('서브')
        select_category.addItem('반찬')
        select_category.addItem('김치')

        menu_label = QLabel('메뉴 이름 :', self)
        menu_lineedit = QLineEdit(self)

        search_button = QPushButton('검색', self)
        search_button.clicked.connect(lambda: self.controller.call_menu_manager(select_time.currentText(), select_category.currentText(), 'search', menu_lineedit.text()))
        search_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        add_button = QPushButton('추가', self)
        add_button.clicked.connect(lambda: self.controller.call_menu_manager(select_time.currentText(), select_category.currentText(), 'add', menu_lineedit.text()))
        add_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        delete_button = QPushButton('삭제', self)
        delete_button.clicked.connect(lambda: self.controller.call_menu_manager(select_time.currentText(), select_category.currentText(), 'delete', menu_lineedit.text()))
        delete_button.clicked.connect(lambda: message.setText(self.controller.get_response()))

        # 수평박스에 구성요소 삽입
        hbox_editmenu_time = QHBoxLayout()
        hbox_editmenu_time.addStretch(1)
        hbox_editmenu_time.addWidget(meal_label)
        hbox_editmenu_time.addWidget(select_time)
        hbox_editmenu_time.addWidget(category_label)
        hbox_editmenu_time.addWidget(select_category)
        hbox_editmenu_time.addWidget(menu_label)
        hbox_editmenu_time.addWidget(menu_lineedit)
        hbox_editmenu_time.addWidget(search_button)
        hbox_editmenu_time.addWidget(add_button)
        hbox_editmenu_time.addWidget(delete_button)
        hbox_editmenu_time.addStretch(1)

        # 그룹박스에 위에서 만든 수평박스 삽입
        groupbox_editmenu_time.setLayout(hbox_editmenu_time)

        # 메뉴 추가 / 삭제 (밥/죽) 그룹박스
        groupbox_editmenu_rp = QGroupBox('메뉴 추가 / 삭제 (밥/죽)')
        
        # 메뉴 추가 / 삭제 (밥/죽) 수평박스 구성요소
        rp_label = QLabel('종류 :', self)
        select_rp = QComboBox(self)
        select_rp.addItem('밥/죽')
        category_rp_label = QLabel('카테고리 : ', self)
        select_category_rp = QComboBox(self)
        select_category_rp.addItem('밥')
        select_category_rp.addItem('죽')

        rp_menu_label = QLabel('메뉴 이름 :', self)
        rp_menu_lineedit = QLineEdit(self)

        rp_search_button = QPushButton('검색', self)
        rp_search_button.clicked.connect(lambda: self.controller.call_menu_manager(select_rp.currentText(), select_category_rp.currentText(), 'search', rp_menu_lineedit.text()))
        rp_search_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        rp_add_button = QPushButton('추가', self)
        rp_add_button.clicked.connect(lambda: self.controller.call_menu_manager(select_rp.currentText(), select_category_rp.currentText(), 'add', rp_menu_lineedit.text()))
        rp_add_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        rp_delete_button = QPushButton('삭제', self)
        rp_delete_button.clicked.connect(lambda: self.controller.call_menu_manager(select_rp.currentText(), select_category_rp.currentText(), 'delete', rp_menu_lineedit.text()))
        rp_delete_button.clicked.connect(lambda: message.setText(self.controller.get_response()))

        hbox_editmenu_rp = QHBoxLayout()
        hbox_editmenu_rp.addStretch(1)
        hbox_editmenu_rp.addWidget(rp_label)
        hbox_editmenu_rp.addWidget(select_rp)
        hbox_editmenu_rp.addWidget(category_rp_label)
        hbox_editmenu_rp.addWidget(select_category_rp)
        hbox_editmenu_rp.addWidget(rp_menu_label)
        hbox_editmenu_rp.addWidget(rp_menu_lineedit)
        hbox_editmenu_rp.addWidget(rp_search_button)
        hbox_editmenu_rp.addWidget(rp_add_button)
        hbox_editmenu_rp.addWidget(rp_delete_button)
        hbox_editmenu_rp.addStretch(1)

        # 그룹박스에 위에서 만든 수평박스 삽입
        groupbox_editmenu_rp.setLayout(hbox_editmenu_rp)

        # 메뉴 추가 / 삭제 (간식) 그룹박스
        groupbox_editmenu_snack = QGroupBox('메뉴 추가 / 삭제 (간식)')
        
        # 메뉴 추가 / 삭제 (간식) 수평박스 구성요소
        snack_label = QLabel('종류 :', self)
        select_snack = QComboBox(self)
        select_snack.addItem('간식')
        category_snack_label = QLabel('카테고리 : ', self)
        select_category_snack = QComboBox(self)
        select_category_snack.addItem('간식')

        snack_menu_label = QLabel('메뉴 이름 :', self)
        snack_menu_lineedit = QLineEdit(self)

        snack_search_button = QPushButton('검색', self)
        snack_search_button.clicked.connect(
            lambda: self.controller.call_menu_manager(select_snack.currentText(), select_category_snack.currentText(),
                                                      'search', snack_menu_lineedit.text()))
        snack_search_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        snack_add_button = QPushButton('추가', self)
        snack_add_button.clicked.connect(
            lambda: self.controller.call_menu_manager(select_snack.currentText(), select_category_snack.currentText(),
                                                      'add', snack_menu_lineedit.text()))
        snack_add_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        snack_delete_button = QPushButton('삭제', self)
        snack_delete_button.clicked.connect(
            lambda: self.controller.call_menu_manager(select_snack.currentText(), select_category_snack.currentText(),
                                                      'delete', snack_menu_lineedit.text()))
        snack_delete_button.clicked.connect(lambda: message.setText(self.controller.get_response()))

        hbox_editmenu_snack = QHBoxLayout()
        hbox_editmenu_snack.addStretch(1)
        hbox_editmenu_snack.addWidget(snack_label)
        hbox_editmenu_snack.addWidget(select_snack)
        hbox_editmenu_snack.addWidget(category_snack_label)
        hbox_editmenu_snack.addWidget(select_category_snack)
        hbox_editmenu_snack.addWidget(snack_menu_label)
        hbox_editmenu_snack.addWidget(snack_menu_lineedit)
        hbox_editmenu_snack.addWidget(snack_search_button)
        hbox_editmenu_snack.addWidget(snack_add_button)
        hbox_editmenu_snack.addWidget(snack_delete_button)
        hbox_editmenu_snack.addStretch(1)

        # 그룹박스에 위에서 만든 수평박스 삽입
        groupbox_editmenu_snack.setLayout(hbox_editmenu_snack)

        # 알림 그룹박스
        groupbox_message = QGroupBox('알림')
        message = QTextEdit()
        vbox_message = QVBoxLayout()
        vbox_message.addWidget(message)
        groupbox_message.setLayout(vbox_message)
        groupbox_message.setMinimumHeight(250)

        # 관리자 그룹박스
        groupbox_admin = QGroupBox('관리자 모드 진입')
        pass_label = QLabel('Password : ')
        pass_lineedit = QLineEdit()
        pass_lineedit.setEchoMode(QLineEdit.Password)
        login_button = QPushButton('로그인', self)
        login_button.clicked.connect(lambda: self.controller.try_login(pass_lineedit.text()))
        login_button.clicked.connect(lambda: message.setText(self.controller.get_response()))
        vbox_admin = QVBoxLayout()
        vbox_admin.addWidget(pass_label)
        vbox_admin.addWidget(pass_lineedit)
        vbox_admin.addWidget(login_button)
        groupbox_admin.setLayout(vbox_admin)

        grid = QGridLayout()

        grid.addWidget(groupbox_make_search, 0, 0)
        grid.addWidget(groupbox_editmenu_time, 1, 0)
        grid.addWidget(groupbox_editmenu_rp, 2, 0)
        grid.addWidget(groupbox_editmenu_snack, 3, 0)
        grid.addWidget(groupbox_message, 4, 0)
        grid.addWidget(groupbox_admin, 5, 0)
        self.setLayout(grid)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
