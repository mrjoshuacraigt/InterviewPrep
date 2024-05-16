def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1], arr[j] = arr[j], key
            j -= 1


if __name__ == '__main__':
    array = [23, 1, 10, 5, 2]
    insertion_sort(array)
    print(array)
