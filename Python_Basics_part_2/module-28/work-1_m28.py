class File:
    def __init__(self, name: str, mode: str):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.name, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.name, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is OSError:
            return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!')