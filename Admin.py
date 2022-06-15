from datetime import datetime


class Admin:
    def __init__(self):
        self.password = '20181610'
        self.result = ''
        self.logs = ''
        self.response = ''
        self.error = 0
        self.error_message = ''

    def check_password(self, password):
        if self.password == password:
            self.response = '로그인 성공!\n\n'
            self.error = 0
            self.get_logs()
        else:
            now = datetime.now()
            self.error += 1
            self.error_message = now.strftime('%Y-%m-%d %H시 %M분 %S초에 ') + '로그인 오류 발생'
            self.response = '비밀번호가 틀렸습니다'

    def get_logs(self):
        f = open('./Error/Error.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        if len(lines) == 0:
            self.response += '오류 기록이 없습니다.'
            return
        limit = 5
        if len(lines) < limit:
            for l in lines:
                self.response += l
            self.response += '\n최근 %d건의 오류 기록입니다. %d건의 기록만 존재합니다.' % (len(lines), len(lines))
        else:
            i = 0
            while i != limit:
                self.response += lines[len(lines) - limit + i]
                i += 1
            self.response += '\n최근 %d건의 오류 기록입니다.'%(limit)

    def get_error(self):
        return self.error

    def get_error_message(self):
        return self.error_message

    def get_response(self):
        return self.response
