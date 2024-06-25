import heapq

if __name__ == '__main__':
    l = [9,8,7,6,543,2,1]

    print(l)
    heapq.heapify(l)
    print(l)

    print(l[0])
    print(heapq.heappop(l))
    print(l)