import heapq
import math


def points(list, k):
    heap = []

    for x, y in list:
        distance = math.sqrt(x ** 2 + y ** 2)
        heap.append((distance, x, y))

    heapq.heapify(heap)

    res = []

    for _ in range(k):
        _, x, y = heapq.heappop(heap)
        res.append([x, y])
    return res


if __name__ == '__main__':
    coords = [[0, 2], [2, 2]]
    k = 1

    print(points(coords, k))
