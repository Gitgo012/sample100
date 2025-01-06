from collections import deque
def bfs_with_costs(adjacency_mat,start,goal):
    n=len(adjacency_mat)
    cost = [float('inf')]*n
    cost[start]=0
    queue = deque([start])
    predecessor= [-1]*n
    while queue:
        node=queue.popleft()
        for neighbour in range(n):
            if adjacency_mat[node][neighbour] >0:
                new_cost = cost[node]+adjacency_mat[node][neighbour]

                if  new_cost < cost[neighbour]:
                    cost[neighbour] = new_cost
                    predecessor[neighbour] = node
                    queue.append(neighbour)
    path=[]
    current=goal
    if cost[goal]==float('inf'):
        return None, cost[goal]
    while current!=-1:
        path.append(current)
        current=predecessor[current]
    path.reverse()
    return path,cost[goal]

adjacency_mat=[[0,1,1,0,0],[1,0,1,1,1],[1,1,0,0,1],[0,1,0,0,1],[0,1,1,1,0]]
start=0
end=4
path,cost=bfs_with_costs(adjacency_mat,start,end)

if path:
    print("Shortest path:", path)
    print("cost:",cost)
else:
    print("error")

