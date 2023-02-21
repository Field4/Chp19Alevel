def bubblesort(a):
    length = len(a) - 1
    swap = True
    while swap:
        swap = False
        for i in range(length):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                swap = True
        i -= 1


def insertionsort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j] = temp
