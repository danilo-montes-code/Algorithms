from typing import Any

def merge_sort(array: list[Any]) -> None:
    if len(array) < 2:
        return
    
    mid = len(array) // 2
    left_side = array[:mid]
    right_side = array[mid:]

    merge_sort(left_side)
    merge_sort(right_side)

    l = r = curr = 0

    while l < len(left_side) and r < len(right_side):
        if left_side[l] < right_side[r]:
            array[curr] = left_side[l]
            l += 1
        else:
            array[curr] = right_side[r]
            r += 1
        curr += 1

    while l < len(left_side):
        array[curr] = left_side[l]
        l += 1
        curr += 1

    while r < len(right_side):
        array[curr] = right_side[r]
        r += 1
        curr += 1

array = [2, 5, 1, 6, 3, 8, 19, 4]
print(array)
merge_sort(array)
print(array)