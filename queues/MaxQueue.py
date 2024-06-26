from collections import deque


class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.maxQueue = deque()

    def maxValue(self) -> int:
        if self.maxQueue:
            return self.maxQueue[0]

    def enQueue(self, value: int) -> None:
        self.queue.append(value)
        while self.maxQueue:
            last_value = self.maxQueue[-1]
            if value > last_value:
                self.maxQueue.pop()
            else:
                break
        self.maxQueue.append(value)

    def deQueue(self) -> int:
        if self.queue:
            curr = self.queue.popleft()
            curr_max = self.maxQueue[0]
            if curr == curr_max:
                self.maxQueue.popleft()

            return curr


#         curr = 18
#         max  = 18


if __name__ == '__main__':
    q = MaxQueue()
    q.enQueue(20)
    print(q.maxValue())
    print(q.maxQueue)
    q.enQueue(15)
    q.enQueue(15)
    q.enQueue(16)
    q.enQueue(12)
    q.enQueue(11)
    q.deQueue()
    q.deQueue()
    print(q.maxQueue)
    print(q.maxValue())

