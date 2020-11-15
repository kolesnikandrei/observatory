import time

NoResult = None


class Task:
    def __init__(self):
        self.ready = False
        self.result = NoResult

    def run(self) -> None:
        raise NotImplementedError


class Sleep(Task):
    def __init__(self, duration, result=None):
        super().__init__()
        self.threshold = time.time() + duration
        self.result = result

    def run(self):
        now = time.time()
        if now >= self.threshold:
            self.ready = True
