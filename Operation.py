import ComputationalGraph
import abc

class Operation:
    def __init__(self, input_nodes=[]):
        self.input_nodes = input_nodes

        input_names = [a.__name__  for a in input_nodes]

        self.__name__ = " ".join(input_names) + " "+ self.__class__.__name__
        self.users = []
        for input_node in input_nodes:
            input_node.users.append(self)

        ComputationalGraph.computational_graph.operations.append(self)
        ComputationalGraph.computational_graph.names[self.__name__] = self.__class__.__name__

    @abc.abstractmethod
    def compute(self):
        pass
