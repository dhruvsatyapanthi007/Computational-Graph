import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict

from Operation import Operation
from PlaceHolder import placeholder
from Variable import Variable
from Constant import Constant
import ComputationalGraph

class Session:
    def run(self, operation, feed_dict={}):
        g_val = nx.DiGraph()
        g_var = nx.DiGraph()

        nodes_porder = porder_trav(operation)
        labels_dict_2 = ComputationalGraph.computational_graph.names

        label_dict_1 = {}
        edges = []

        for i, curr_node in enumerate(nodes_porder):
            if isinstance(curr_node, placeholder):
                curr_node.output = feed_dict[curr_node]
            elif isinstance(curr_node, Variable):
                curr_node.output = curr_node.value
            elif isinstance(curr_node, Constant):
                curr_node.output = curr_node.value
            else:
                curr_node.inputs = [curr_node_input.output for curr_node_input in curr_node.input_nodes]
                curr_node.output = curr_node.compute(*curr_node.inputs)
                label = labels_dict_2[curr_node.__name__]

                input_names = [node_input.__name__ for node_input in curr_node.input_nodes]

                for node_input in curr_node.inputs:
                    label_dict_1[str(node_input)] = str(node_input)
                    g_val.add_edge(str(node_input), str(label)+'_'+str(i))
                    edges.append((str(node_input), str(label)+'_'+str(i)))

                label_dict_1[str(label)+'_'+str(i)] = str(label)
                label_dict_1[str(curr_node.output)] = str(curr_node.output)
                g_val.add_edge(str(label+'_'+str(i)), str(curr_node.output))
                edges.append((str(label+'_'+str(i)), str(curr_node.output)))

                for input_name in input_names:
                    g_var.add_edge(str(input_name), curr_node.__name__)

            if isinstance(curr_node.output, list):
                curr_node.output = np.array(curr_node.output)

        color_dict = OrderedDict()
        node_size = OrderedDict()
        for k in g_val.nodes():
            if label_dict_1[k] == k:
                color_dict[k] = "tab:green"
                node_size[k] = 400
            else:
                color_dict[k] = "tab:blue"
                node_size[k] = 1200

        g_color_val = color_dict.values()
        g_n_size = list(node_size.values())
        nx.draw_networkx(g_val, labels=label_dict_1, with_labels = True, connectionstyle='arc3, rad = 0.1', node_color = g_color_val, node_size = g_n_size)

        plt.savefig("valueEvaluation.png")
        plt.clf()

        #Color
        color_dict = OrderedDict()
        node_size = OrderedDict()
        for k in g_var.nodes():
            if labels_dict_2[k] == k:
                color_dict[k] = "tab:green"
                node_size[k] = 400
            else:
                color_dict[k] = "tab:blue"
                node_size[k] = 1200

        color_val = color_dict.values()
        node_size_val = list(node_size.values())

        nx.draw_networkx(g_var, labels=labels_dict_2, with_labels = True, connectionstyle='arc3, rad = 0.1', node_color = color_val, node_size = node_size_val)
        plt.savefig("OrderOfOps.png")

        return operation.output


def porder_trav(operation):
    nodes_porder = []

    def find_inputs(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                find_inputs(input_node)
        nodes_porder.append(node)

    find_inputs(operation)
    return nodes_porder