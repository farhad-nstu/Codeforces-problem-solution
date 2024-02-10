import collections

class bfs_traverse:
    def __init__(self):
        self.graph = {0: [1, 2],
                    1: [0, 3, 4],
                    2: [0, 5, 6],
                    3: [1, 7, 8],
                    4: [3],
                    5: [],
                    6: [],
                    7: [],
                    8: []
                }
        self.visited = set()
        self.res = []
    
    def bfs(self, start):
        # q = collections.deque([start])
        q = [start]
        self.visited.add(start)  

        while q:
            # vertex = q.popleft()
            vertex = q.pop(0)
            self.res.append(vertex)
            for next in self.graph[vertex]:
                if next not in self.visited:
                    self.visited.add(next)
                    q.append(next)

obj = bfs_traverse()
obj.bfs(0)
print(obj.res)


# class Node:
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
    
# def bfsTraverse(root):
#     q = []
#     q.append(root)

#     while len(q):
#         print(q[0].data, " ")
#         root = q.pop(0)

#         if root.left:
#             q.append(root.left)
        
#         if root.right:
#             q.append(root.right)