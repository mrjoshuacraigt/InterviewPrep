


def quickSortRecursive(array: [int], l:int = None, r: int = None):
    if array is None or len(array) <= 1:
        return

    if l is None:
        l = 0

    if r is None:
        r = len(array) - 1

    if l >= r:
        return

    pivot = array[r]

    # doing sorting
    i = l

    for j in range(l, r):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    # swap pivot
    array[i], array[r] = array[r], array[i]




    # call quicksort on left and right
    quickSortRecursive(array, l,  i - 1)
    quickSortRecursive(array, i + 1, j)



def quickSortIterative(array, k) -> int:
    if array is None:
        return

    itarget = len(array) - k


    stack = []
    stack.append(0)
    stack.append(len(array) - 1)

    while stack:
        ihi = stack.pop()
        ilo = stack.pop()

        pivot = array[ihi]
        i = ilo
        for j in range(ilo, ihi):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1

        # swap pivot
        array[i], array[ihi] = array[ihi], array[i]

        if i == itarget:
            return array[i]

        elif i < itarget:
            stack.append(i + 1)
            stack.append(len(array) - 1)
        else:
            stack.append(0)
            stack.append(i -1)





if __name__ == '__main__':
    arr = [88,55,3,2,1]
    # quickSortRecursive(arr)
    print(arr)

    print(quickSortIterative(arr, 1))
    print(quickSortIterative(arr, 2))
    print(quickSortIterative(arr, 3))
    print(quickSortIterative(arr, 4))
    print(quickSortIterative(arr, 5))



