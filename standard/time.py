from interpreter import Callable
import time

class Time(Callable):
    def __init__(self):
        super().__init__()
        self.arity = 0

    def call(self, interpreter, args):
        return time.time()

