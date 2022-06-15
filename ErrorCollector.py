class ErrorCollector:
    def __init__(self):
        self.filepath = './Error/Error.txt'

    def logging(self, message):
        f = open(self.filepath, 'a', encoding='utf-8')
        f.write(message + '\n')
        f.close()
