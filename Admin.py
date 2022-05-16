class Admin:
    def __init__(self):
        self.password = '20181610'
        self.result = ''
        self.error = 0
        self.get_error()

    def check_password(self, password):
        if self.password == password:
            self.result = '로그인 성공\n'
            self.get_error()
            self.result += '현재까지 오류 횟수 : ' + str(self.error)
        else:
            self.result = '비밀번호가 틀렸습니다'
            self.update_error(1)

    def get_result(self):
        return self.result

    def get_error(self):
        f = open('./Error/Error.txt', 'r')
        self.error = int(f.readline())
        f.close()
        return self.error

    def update_error(self, error_num):
        error = self.get_error() + error_num
        f = open('./Error/Error.txt', 'w')
        f.write(str(error))
        f.close()
