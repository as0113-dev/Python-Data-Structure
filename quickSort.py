def quickSort(array):
    #base case if array has only 1 element then return the array
    if len(array) < 2:
        return array

    #pivot is last element in array
    pivot = array[-1]

    #partition array into left and right
    #left = all values of arr[i] <= pivot
    #right = all values of arr[i] > pivot
    left = [array[i] for i in range(len(array)-1) if array[i] <= pivot]
    right = [array[i] for i in range(len(array)-1) if array[i] > pivot]

    #recurse call on left concatinated with [pivot] then concatinate the recurse call on right
    return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([1,2,6,4,5,3])) #outputs [1,2,3,4,5,6]
print(quickSort([20,50,5,22,35,40])) #outputs [5,20,22,35,40,50]
