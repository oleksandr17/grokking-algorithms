def sum(list):
    if len(list) == 0:
        return 0
    first = list.pop(0)
    return first + sum(list)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(sum(my_list))
    my_list = [1]
    print(sum(my_list))
    my_list = []
    print(sum(my_list))
