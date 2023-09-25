# Selection Sort

## General Idea
In selection sort, we have the concepts of the sorted and unsorted parts of the array. We find the index of the minimum value in the array, and swap it with the first element of the unsorted portion of the array. In this way, we `"select"` the smallest element and put it in the front of the list.

# TODO
**First Iteration**:
1. Starting with the first element of the array, we compare the element to the next one in the array.
2. If the current element is greater than the next, we swap the two elements.
3. We then move to the second element, and make the same comparison to the following element.
4. This is repeated until the end of the array is reached.
5. At this point, the last element is the largest element in the array.
This begins the sorted portion of the array.

**Second Iteration**:
1. We again start with the first element in the array, making the same comparisons as in the first iteration.
2. However, we only compare up to the sorted portion of the array, which on this iteration is the second to last element.

**N-th Iteration**:
1. Starting with the first element in the array, compare the element to the following element.
2. If the current element is greater than the following one, swap the two.
3. Move to the next element in the array, performing the same comparision with its following element.
4. Do this until you reach the position of `len(array) - n`, which begins the sorted portion of the array.
# ENDTODO

## Key Qualities
In-Place? - Yes \
Stable?   - No \
Time Complexity  = O(n^2),
                    n - number of elements in the array \
-> Each iteration, we run through the array from beginning to the end of the unsorted portion. We perform these iterations once for every element in the array, giving us a nested loop of n * n time \
Space Complexity = O(1), 
                    in-place: no extra memory is used