from interpreter import Callable
import time

class Time(Callable):
    def __init__(self):
        super().__init__()

    def call(self, *args, **kwargs):
        return time.time()
