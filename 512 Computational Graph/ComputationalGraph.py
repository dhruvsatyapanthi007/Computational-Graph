class ComputationalGraph:
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
        self.names = {}

    def set_default(self):
        global computational_graph
        computational_graph = self
