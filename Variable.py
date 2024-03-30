import ComputationalGraph

class Variable:
    def __init__(self, value, name=''):
        self.value = value
        self.users = []
        self.__name__ = name

        ComputationalGraph.computational_graph.variables.append(self)
        ComputationalGraph.computational_graph.names[self.__name__] = self.__name__
