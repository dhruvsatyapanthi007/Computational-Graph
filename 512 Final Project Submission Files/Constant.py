import ComputationalGraph

class Constant:
    def __init__(self, value):
        self.value = value
        self.users = []
        self.__name__ = str(round(self.value, 2))

        ComputationalGraph.computational_graph.variables.append(self)
        ComputationalGraph.computational_graph.names[self.__name__] = self.__name__
