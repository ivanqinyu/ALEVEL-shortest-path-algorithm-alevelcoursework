import numpy as np

def ConstructPath(graph, i, j):
    i,j = int(i), int(j)
    if(i==j):
      print (i,)
    elif(graph[i,j] == -30000):
      print (i,'-',j)
    else:
      ConstructPath(graph, i, graph[i,j]);
      print(j,)

graph = np.array([[0,10,5,8,999999],
                  [10,0,999999,999999,9],
                  [5,999999,0,2,5],
                  [8,999999,2,0,999999],
                  [999999,9,999999,999999,0]])

print("graph = ")
v = len(graph)
for i in range(0,v):
    for j in range(0,v):
        if graph[i,j]==999999:
            print("  ∞,",end=" ")
        else:
            print (" ",graph[i,j],end=", ")
    print()
    
for k in range(0,v):
    for i in range(0,v):
        for j in range(0,v):
            if graph[i,j] > graph[i,k] + graph[k,j]:
                graph[i,j] = graph[i,k] + graph[k,j]
                print("k=",k," i=",i," j=",j)
                for i in range(0,v):
                    for j in range(0,v):
                        if graph[i,j]==999999:
                            print("  ∞",end=", ")
                        else:
                            print (" ",graph[i,j],end=", ")
                    print()
    

print("graph = ",graph)

#ConstructPath(graph,0,4)
