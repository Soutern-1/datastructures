class Graph():
    def __init__(self,maxnodecount):
        self.maxnodecount = maxnodecount
        self.neighbours = [[]* maxnodecount for i in range(self.maxnodecount)]
    
    def add_edges(self,end1,end2):
        self.neighbours[end1].append(end2)
        self.neighbours[end2].append(end1)
    
    def breath_search(self,start):
        queue = []
        complete = []
        visited_list = []

        for i in range (self.maxnodecount):
            complete.append(False)
        print(complete)
        queue.append(start)
        visited_list.append(start)
        complete[start] = True
        while queue:
            start = queue.pop(0)
            print(start)
            for f in self.neighbours[start]:
                if not complete[f]:
                        queue.append(f)
                        visited_list.append()
                        complete[f] = True
                

            
            print("***")
            print(queue)
            print(complete)
            

        
        print(visited_list)

                    




        

graph = Graph(5)

print(graph.neighbours)
graph.add_edges(0,1)
graph.add_edges(2,3)
graph.add_edges(0,4)
graph.add_edges(0,2)
graph.add_edges(2,4)
graph.add_edges(0,3)

print(graph.neighbours)

graph.breath_search(0)

