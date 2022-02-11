# Graph class will represent the matrix table of distance tables
# it needs to have a list of vertices: Address (Adjacency list)
# a 2d array of edge_list

class Graph():
    def __init__(self):
        # initialize an empty dictionary that will hold vertices. In this case it would be the locations
        self.vertex_list = {}
        # initialize an empty list that will hold a key value pair key: (location_a, location b) value: weights (distance)
        self.edge_weights = {}

    # To do: create a method that will load the a vertex_list each with its own
    def addVertex(self, vertex):
        # each vertex should have a list of distances
        self.vertex_list[vertex] = []
