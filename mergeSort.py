def mergeSort(array):
    #base case
    if len(array) <= 1:
        return array
    #midpoint of "array"
    mid = len(array)//2

    #split array in half
    leftSplit = array[:mid]
    rightSplit = array[mid:]

    #recursively call the splitting of array
    leftArray = mergeSort(leftSplit)
    rightArray = mergeSort(rightSplit)

    #final step call the merge "helper" function that builds the array and sort them
    return merge(leftArray, rightArray)



def merge(leftArr, rightArr):
    #the array that we return in the end after filling it up
    result = [] 
    l_Index, r_Index = 0, 0
    while l_Index < len(leftArr) and r_Index < len(rightArr):
        if leftArr[l_Index] < rightArr[r_Index]:
            result.append(leftArr[l_Index])
            l_Index += 1
        else:
            result.append(rightArr[r_Index])
            r_Index += 1
    if l_Index == len(leftArr):
        result += rightArr[r_Index:]
    else:
        result += leftArr[l_Index:]
    
    return result



list1 = [4,3,2,1]
fixed_list1 = mergeSort(list1)
print(fixed_list1)