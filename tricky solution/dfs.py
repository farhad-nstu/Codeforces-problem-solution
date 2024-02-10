class death_first_search:
    def __init__(self):
        self.graph = {0: [1, 2],
                    1: [0, 3, 4],
                    2: [0, 5, 6],
                    3: [1, 7, 8],
                    4: [3, 10],
                    5: [9],
                    6: [],
                    7: [],
                    8: [],
                    9: [],
                    10: [],
                }
        # self.visited = set()
        self.res = []
    
    def dfs(self, start):
        # self.visited.add(start)
        self.res.append(start)
        
        for next in self.graph[start]:
            if next not in self.res:
                self.dfs(next)

obj = death_first_search()
obj.dfs(0)
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

# def dfsTraverse(root):
#     if not root:
#         return


#     print(root.data, " ")
    
#     if root.left:
#         dfsTraverse(root.left)
    
#     if root.right:
#         dfsTraverse(root.right)

# if __name__ == "__main__":
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     # bfsTraverse(root)
#     dfsTraverse(root)