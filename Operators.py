from Operation import Operation
import numpy as np

class sub(Operation):
    def __init__(self, x, y):        
        super().__init__([x, y])

    def compute(self, x_value, y_value):
        return x_value - y_value

class mul(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_value, y_value):
        return x_value * y_value

class div(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_value, y_value):
        return x_value / y_value

class modulo(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])
        
    def compute(self, x_value, y_value):
        return x_value % y_value

class power(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_value, y_value):
        return x_value ** y_value

class matTranspose(Operation):
    def __init__(self, a):
        super().__init__([a])

    def compute(self, a_value):
        return np.transpose(a_value)

class matInversion(Operation):
    def __init__(self, a):
        super().__init__(a)

    def compute(self, a_value):
        return np.linalg.inv(a_value)

class matmul(Operation):
    def __init__(self, a, b):
        super().__init__([a, b])

    def compute(self, a_value, b_value):
        return a_value.dot(b_value)

class add(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])
        
    def compute(self, x_value, y_value):
        return (x_value + y_value)
