class vertex:
    def __init__(self):
        # A vertex will have it's own value as well as the edges to it
        pass


class AdjacenyMatrix:
    def __init__(self, n):
        # n is the number of nodes => So we'll have a nxn matrix 
        self.adjacenyMatrix = [ [-1]*5 for _ in range(5)]

    def addEdge(self, v1, v2):
        # Creating a edge between node/vertex v1 and v2 ... indexing is started from 0 here
        self.adjacenyMatrix[v1-1][v2-1] = 1
        self.adjacenyMatrix[v2-1][v1-1] = 1

    def print_matrix(self):
        for i in self.adjacenyMatrix:
            print(i)
        
       

matrix_1 = AdjacenyMatrix(5)  
matrix_1.addEdge(1,2)
matrix_1.addEdge(3,5)
matrix_1.addEdge(3,2)
matrix_1.addEdge(2,4)
matrix_1.addEdge(2,2)
matrix_1.print_matrix()

