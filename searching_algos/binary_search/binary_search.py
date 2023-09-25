

def binary_search(array: list, target) -> int:

    l, r = 0, len(array)

    while l <= r:

        mid = (l + r) // 2

        if array[mid] == target:
            return mid
        if array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1