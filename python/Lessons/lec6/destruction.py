
class Life:
    def __init__(self, name):
        self.name = name
        print(f"Hi, {self.name}")
        # return name

    def __del__(self):
        print(f'GOODBYE {self.name}')
