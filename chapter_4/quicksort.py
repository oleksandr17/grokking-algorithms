def quicksort(list):
    if len(list) < 2:
        return list
    pivot = list[0]
    less = [item for item in list[1:] if item < pivot]
    greater = [item for item in list[1:] if item >= pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    my_list = []
    print(quicksort(my_list))
    my_list = [4,3]
    print(quicksort(my_list))
    my_list = [4,3,1]
    print(quicksort(my_list))
    my_list = [4,3,1,7]
    print(quicksort(my_list))
    my_list = [4,3,1,7,56,88,7,67,44,99,0,65,43,56,76,21,43,65,98]
    print(quicksort(my_list))
