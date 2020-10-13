'''
Bubble sort algorithm swaps elements adjacent. 
Big O notation is O(n^2)
first for loop runs thrugh array n number of times
second for loop inside the 1st for loop runs n-1 times
'''

list1 = [9, 5, 8, 1, 6, 3, 2, 0]
def bubbleSort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i- 1):
            count +=1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                #or we can swap by saying
               # arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print("Count =", str(count))


#testing bubble sort function
print("Pre-Sort: " + str(list1))
bubbleSort(list1)
print("Post-Sort: " + str(list1))
