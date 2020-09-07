

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if  arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))    #list.pop(index)————删除并返回list中索引为index的值
    return newArr

def quicksort(arr):
    if  len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for  i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def print_items(list):
    for item in list:
        print(item)

print(quicksort([5,3,6,2,10,7,14,65]))