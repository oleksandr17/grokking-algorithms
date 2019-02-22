def findSmallestIndex(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallestIndex(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == "__main__":
    my_list = [4,3,1,7,56,88,7,67,44,99,0,65,43,56,76,21,43,65,98]
    print(selectionSort(my_list))
