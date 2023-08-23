def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array) - i):
            if j == len(array) - 1:
                continue
                
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        
    return array



print(bubble_sort([2, 3, 6, 7, 1, 8, 10]))
print(bubble_sort([1, 2, 7, 6, 3, 1, 8, 2]))
print(bubble_sort([(1, 0), (1, 2), (4, 0), (1, 1)]))