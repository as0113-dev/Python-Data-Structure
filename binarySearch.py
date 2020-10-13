'''

[ 1, 3, 5, 7, 8, 10, 30 ]
  0  1  2  3  4   5   6

'''
def binarySearch(array, key):

    high, low = len(array)-1, 0
    while low <= high:
        mid = (high+low)//2
        if array[mid] == key:
            return "found key at index %d" % mid
        elif array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return "the key: \"%s\" not found" % key


def recursiveBinarySearch(array, key, high, low):
    #base case
    if low > high:
        return "not found"
    
    mid = (high + low) //2
    if array[mid] == key:
        return "found key at index %d" % mid
    elif array[mid] > key:
        return recursiveBinarySearch(array, key, mid-1, low)
    else:
        return recursiveBinarySearch(array, key, high, mid+1)


print(binarySearch([1,5,10,15,20], 20))
print(recursiveBinarySearch([1,5,10,15,20], 20, 4, 0))

#how can I fix this code to where it can be more efficiently tested by multiple users?
