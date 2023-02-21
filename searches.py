def linear_search(array, item):
    i = 0
    for i in range(len(array)):
        if array[i] == item:
            return True
    return False


def binary_search(array, item):

    lowerbound = 0
    upperbound = len(array)
    while lowerbound <= upperbound:
        index = int((lowerbound + upperbound) / 2)
        if array[index] == item:
            return True
        elif array[index] < item:
            lowerbound = index + 1
        else:
            upperbound = index - 1
    return False


values = [1, 4, 67, 35, 49, 69, 84, 325, 84]
sorted_values = [1, 2, 5, 8, 34, 36, 45, 49, 56, 78, 90]
if linear_search(values, 49):
    print("Linear")

if binary_search(sorted_values, 49):
    print("binary")
