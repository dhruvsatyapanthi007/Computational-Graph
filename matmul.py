from Operation import Operation

class matmul(Operation):
    """Multiplies matrix a by matrix b, producing a * b.
    """
    
    # def __init__(self, a, b):
    def __init__(self, a, b):
        super().__init__([a, b])

    def compute(self, a_value, b_value):
        """Compute the output of the matmul operation

        Args:
          a_value: First matrix value
          b_value: Second matrix value
        """
        return a_value.dot(b_value)