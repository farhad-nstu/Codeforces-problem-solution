class PriorityQueue(object):
    def __init__(self) -> None:
        self.arr = []

    def insert(self, newNum):
        self.arr.append(newNum)
    
    def empty(self):
        return len(self.arr) == 0

    def takeAndRemove(self):
        max_val_idx = 0
        for i in range(len(self.arr)):
            if self.arr[i] > self.arr[max_val_idx]:
                max_val_idx = i
                
        max_val = self.arr[max_val_idx]
        self.arr.remove(max_val)
        return max_val

t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    arr = list(map(int, input().split()))
    pr_queue = PriorityQueue()
    res = 0
    for i in range(n):
        if arr[i] == 0:
            if pr_queue.empty():
                continue
            res += pr_queue.takeAndRemove()
        else:
            pr_queue.insert(arr[i])
    print(res)
    