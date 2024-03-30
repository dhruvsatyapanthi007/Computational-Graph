import ComputationalGraph

class placeholder:
    """Represents a placeholder node that has to be provided with a value
       when computing the output of a computational graph
    """

    def __init__(self, name):
        self.users = []

        # Append this placeholder to the list of placeholders in the currently active default graph
        ComputationalGraph.computational_graph.placeholders.append(self)
        self.__name__ = name
        ComputationalGraph.computational_graph.names[self.__name__] = name
