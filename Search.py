import sys
from collections import deque
from operator import itemgetter
import heapq

##Breadth first search                                                                                                                                                                                      
def BFS(graph, start, end):

    visited, queue, path = [], [], []

    queue.append([start])

    while (len(queue) > 0):


        path = queue.pop(0)

        node = path[-1]


        if node == end:
            return path

        elif node not in visited:
            for vertex in graph:
                if vertex[0] == node:

                    for x in range(1, len(vertex)):

                        path2 = list(path)
                        path2.append(vertex[x])
                        queue.append(path2)

            visited.append(node)

    return (path)

## Depth first search                                                                                                                                                                                       
def DFS(graph, start, end, path = None):

    visited, stack, path = [], [], []
    stack.append(start)

    if(start == end):
        path.append(start)
        return path

    else:
        while (len(stack) > 0):
        
            node = stack.pop()
            visited.append(node)
            path.append(node)
        
            if node == end:
              return path

            else:
                for vertex in graph:
                    if vertex[0] == node:
                        for x in range(1, len(vertex)):
                             if vertex[x] not in visited:
                                stack.append(vertex[x])
 
    return (path)


## uniform cost search                                                                                                                                                                                      
def UCS(edges, graph, start, end):

    visited, queue, path = [], [], []
    queue.append([start])

    while (len(queue) > 0):
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path

        elif node not in visited:
            for vertex in graph:
                if vertex[0] == node:

                    for x in range(1, len(vertex)):

                        path2 = list(path)
                        path2.append(vertex[x])
                        queue.append(path2)

            visited.append(node)

    return (path)

# This function reads data from file and creates graph                                                                                                                                                      
def readFromFile(fileName):

    edges = []
    neighbors = []
    input_file = open(fileName, 'r')
    tempList = []
    for line in input_file:
        node1, node2, w = line.split()
        tempList.append((node1, node2, int(w)))
    edges = sorted(tempList, key = itemgetter(2))

    nodesList = []
    for edge in edges:
        if edge[0] not in nodesList:

            nodesList.append(edge[0])

    temp = []
    for node in nodesList:
        temp.append(node)
        for edge in edges:
            if edge[0] == node:
                temp.append(edge[1])

        neighbors.append(temp)
        temp = []

    input_file.close()


    return (edges, neighbors)
    
def convert( someList ):
    for item in someList:
        try:
            yield int(item)
        except ValueError:
            yield item

def main():
    inputFile  = (sys.argv[1])

    start  = (sys.argv[2])
    end    = (sys.argv[3])
    path = []
    edges, neighbors = readFromFile(inputFile)
    if "BFS" ==str(sys.argv[4]):
        path  = BFS(neighbors, start , end)
        #print (path)                                                                                                                                                                                       
        #print "[%s]" % (','.join(path))
    if "DFS" ==str(sys.argv[4]):
        path = DFS(neighbors, start , end)
        #print (path)                                                                                                                                                                                       
        #print "[%s]" % (','.join(path))
    if "UCS" ==str(sys.argv[4]):
        path = UCS(edges, neighbors, start , end)
        #print "[%s]" % (','.join(path))

    #print "[%s]" % (','.join(path)) 
            #print (path)
    #print (path)        
    #print "[%s]" % (','.join(path)) 
    newList= list( convert( path ) )



    print (newList)
main()

