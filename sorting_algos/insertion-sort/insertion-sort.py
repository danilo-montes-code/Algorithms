############################
##   Iterative Approach   ##
############################

def insertionSortIterative(arr: list) -> list:
    if not arr:
        return []

    # Iterate through array
    for i, num in enumerate(arr):

        # skip the first element, since it can not be compared with anything
        if i == 0:
            continue

        # we iterate backwards until we reach the start
        # using backwards to store the index of the number we are comparing
        backwards = i - 1

        # check if current element is smaller than previous
        while backwards >= 0 and num < arr[backwards]:
            
            # if yes, shift those elements forwards
            arr[backwards + 1] = arr[backwards]
            backwards -= 1

        # insert the element into the array right before the place in 
        # the array that it belongs
        arr[backwards + 1] = num
    
    return arr


inputArr = [3, 8, 5, 4, 1, 9, -2]
print(insertionSortIterative(inputArr))
print(inputArr == [-2, 1, 3, 4, 5, 8, 9])

inputArr = [5, 4, 3, 2, 1]
print(insertionSortIterative(inputArr))
print(inputArr == [1, 2, 3, 4, 5])

inputArr = [8, 4, 6, 2]
print(insertionSortIterative(inputArr))
print(inputArr == [2, 4, 6, 8])


    
############################
##   Recursive Approach   ##
############################

def insertionSortRecursive(arr: list) -> list:
    if not arr:
        return []
    
    for i in range(1, len(arr)):


        def insertionRecursive(backwards, num):    
            if backwards < 0 or num >= arr[backwards]: #base case
                arr[backwards + 1] = num
                return 
            
            arr[backwards + 1] = arr[backwards]
                #recursive call 
            insertionRecursive(backwards - 1, num)

        insertionRecursive(i-1, arr[i])

    return arr

inputArr = [3, 8, 5, 4, 1, 9, -2]
print(insertionSortRecursive(inputArr))
print(inputArr == [-2, 1, 3, 4, 5, 8, 9])

inputArr = [5, 4, 3, 2, 1]
print(insertionSortRecursive(inputArr))
print(inputArr == [1, 2, 3, 4, 5])

inputArr = [8, 4, 6, 2]
print(insertionSortRecursive(inputArr))
print(inputArr == [2, 4, 6, 8])