import math


def binary_search(items, item):
    steps = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        steps += 1
        mid = math.floor((low + high) / 2)
        # print(low, mid, high)
        guess = items[mid]
        if guess == item:
            return mid, steps
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9, 11, 23, 34, 45, 56, 57, 67, 78, 89, 91, 93, 96, 97, 98]
    print (binary_search(my_list, 7))
    print (binary_search(my_list, -1))
