class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def delete(self):
        # try:
        max_val = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max_val]:
                max_val = i
        item = self.queue[max_val]
        del self.queue[max_val]
        return item

t=int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    myQueue = PriorityQueue()
    for i in arr:
        if i == 0:
            if myQueue.isEmpty():
                continue
            res += myQueue.delete()
        else:
            myQueue.insert(i)
    print(res)
    