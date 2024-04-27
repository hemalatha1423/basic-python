def storeBFS(startNode, result, adj, n, visited):
    visited[startNode] = True
    Q = [startNode]
 
    while len(Q) > 0:
        currNode = Q.pop(0)
        result.append(currNode)
 
        for neighbour in adj[currNode]:
            if not visited[neighbour]:
                visited[neighbour] = True
                Q.append(neighbour)

                
def printBFSTraversal(adj, n):
    visited = [False] * (n + 1)  
    result = []
 
    for i in range(1, n+1):  
        if not visited[i]:
            storeBFS(i, result, adj, n, visited)
 
    print(*result)
 

 
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]  
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

printBFSTraversal(adj,n)
