def binarySearch(arr, target) -> int:
    if arr is None:
        return -1

    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
        else:
            return arr[mid]

    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(0, len(array)+ 5):
        print("i = {}".format(i))
        print(binarySearch(array, i))
