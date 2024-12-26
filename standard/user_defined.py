from interpreter import Callable
import storage

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

        value = interpreter.visit_block(self.block)
        return value

