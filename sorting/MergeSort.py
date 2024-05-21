def mergeSort(array: [int]) -> [int]:
    # Base Case array len == 0 or len == 1
    if array is None or len(array) <= 1:
        return array

    # split the array
    middle = len(array) // 2

    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])

    sortedArray = []

    ileft = 0
    iright = 0

    while ileft < len(left) and iright < len(right):
        if left[ileft] < right[iright]:
            sortedArray.append(left[ileft])
            ileft += 1
        else:
            sortedArray.append(right[iright])
            iright += 1

    sortedArray.extend(left[ileft:])
    sortedArray.extend(right[iright:])

    return sortedArray


if __name__ == '__main__':
    print(mergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(mergeSort([10]))
    mergeSort(None)
