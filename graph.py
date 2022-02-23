# -- INFO ---------------
# First Name: Joshua
# Last Name: Corpuz
# Student id#: 001196484
# -- INFO ---------------

# NOTES
# Graph class will represent the matrix table of distance tables
# it needs to have a list of vertices: Address
# it will have a dictionary of {address_a: [address_b, weight], [address_b, weight], .... }
# key = vertex_a; values = list[[vertex_b, distance]]

class Graph():
    def __init__(self):
        # initialize an empty list that will hold the vertices. In this case it would be the locations
        self.vertex_list = []
        # initialize an empty list that will hold a key value pair key = (location_a) and value = [location_b, weight]
        self.edge_weights = {}

    # Function adds a node in the vertex list
    # O(n)
    def add_vertex(self, vertex):
        # check if the vertex is not in the vertex_list already
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
        else:
            print("Vertex: ", vertex, " is in the vertex list already")

    # Function adds an edge weight for the given vertex_a, vertex_b
    # O(n)
    def add_edge_weights(self, vertex_a, vertex_b, weight):
        temp = []
        if vertex_a in self.vertex_list and vertex_b in self.vertex_list:

            if vertex_a not in self.edge_weights:
                temp.append([vertex_b, weight])
                self.edge_weights[vertex_a] = temp

            elif vertex_a in self.edge_weights:
                temp.extend(self.edge_weights[vertex_a])
                temp.append([vertex_b, weight])
                self.edge_weights[vertex_a] = temp

        else:
            print("Nodes are not part of the vertex list")

    # Function prints all Graph object's vertex list
    # Used mostly as a checker to review data
    # O(n)
    def print_vertex_list(self):
        for i in range(len(self.vertex_list)):
            print(self.vertex_list[i])

    # Function prints each of the Graph's keys and list of edge weights
    # Used mostly as a checker to review data
    # O(n)
    def print_edge_weights(self):
        for vertex in self.vertex_list:
            print("key: ", vertex, "values: ", self.edge_weights[vertex], "\n")

    # Function returns the list of edge weights for passed vertex
    # O(n)
    def get_edge_weights(self, vertex_a):
        return self.edge_weights[vertex_a]

    # Function returns a specific edge weight for passed vertex_a and vertex_b
    # O(n)
    def get_edge_weight(self, vertex_a, vertex_b):
        adjacency_list = self.edge_weights[vertex_a]
        for location in adjacency_list:
            if location[0] == vertex_b:
                return [location[1], vertex_b]

    # Functions returns all the data in the graph
    # used mostly as a checker to review data
    # O(n)

    def get_graph(self):
        for node in (self.edge_weights):
            print(node, "--->", [i for i in self.edge_weights[node]], "\n")
