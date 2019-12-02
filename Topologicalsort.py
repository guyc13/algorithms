# Developers: Gal Jacobson - 205585227 , Guy Cohen - 204536221
# Subject: Assigment 2 - Algorithems 1



courses={1:"Discrete1",2:"Discrete2",3:"Algo2",4:"Algo1",5:"Datastructure",6:"introtoComputerScience",7:"Computationalmodels",8:"Computational"}

# The graph is represented by a dictionary
# where the keys are the vertexs and the values
# are lists in size 4
# value[0] - dfs detection time , value[1] dfs finish time , value[2] dfs father vertex , value[4] neighbors list
graph1 = {1:[0,0,None,[2]],
          2:[0,0,None,[3]],
          3:[0,0,None,[8]],
          4:[0,0,None,[7,3]],
          5:[0,0,None,[4]],
          6:[0,0,None,[5]],
          7:[0,0,None,[8]],
          8:[0,0,None,[]]
         }


stack=[]
visited=[]
time = 0

def addNode(graph, nodeId, neighbor=None):
    neighbors= [neighbor]
    graph.update({nodeId : [0,0,None,neighbors]})


def addEadg(graph,src,dst):
    graph.update({src: [0, 0, None, [dst]]})


def dfs(graph):
    """
    This fuction is an implements of the DFS Algorithm
    initialise the graph dfs members
    main loo[ for the dictionary
    :param graph:
    :return:
    """
    for node in graph:
        (graph[node])[0] = 0
        (graph[node])[1] = 0
        (graph[node])[2] = None
    for node in graph:
        if node not in visited:
            DFS_visit(graph,node)


def DFS_visit(graph, u):
    """
    Inner loop of the DFS
    push the vertex by their finish time to a stack
    :param graph:
    :param u :
    :return:
    """
    global time
    visited.append(u)
    time = time + 1
    (graph[u])[0]=time                          #d_time

    for v in (graph[u])[3]:                     #neighbors
        if v not in visited:
            (graph[v])[2]=u                     #fatehr
            DFS_visit(graph, v)
    time = time + 1
    (graph[u])[1] = time  # f_time
    stack.append(u)


def topologicalsort(g, vertex_names ):
    """
    This function calls dfs to modify the vertexs finish time in the graph
    push the vertex to stack order by finish time
    this fuction pop the finish time stack and return the value of the named graph
    :param g - graph:
    :param vertex_names - list of vertexs and textual names :
    """
    dfs(g)
    while len(stack)!=0:
         print(vertex_names[stack.pop()])


if __name__ == '__main__':
    print("Edges list:")
    for i in graph1:
        for j in ((graph1[i])[3]):
            print(courses[i]+ "-> " + str(courses[j]))

    print("\nINPUT graph -> " + str(graph1)) #Before
    print('-' * 20)
    print("\noutput: \n")
    topologicalsort(graph1, courses)  #topologica sort
