from interpreter import Callable
import storage


class ReturnException(Exception):
    def __init__(self, result):
        self.result = result

class UserDefined(Callable):
    def __init__(self, arguments, block):
        super().__init__()
        self.arguments = arguments
        self.block = block
        self.arity = len(arguments)

    def call(self, interpreter, arguments):
        interpreter.current_storage = storage.Storage(interpreter.current_storage)
        for i in range(len(self.arguments)):
            interpreter.current_storage.add_value(arguments[i], self.arguments[i])
        try:
            value = interpreter.visit_block(self.block)
        except ReturnException as e:
            interpreter.current_storage = interpreter.current_storage.parent
            return e.result
        interpreter.current_storage = interpreter.current_storage.parent
        return value

