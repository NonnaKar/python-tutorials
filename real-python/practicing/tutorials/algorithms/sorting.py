
# * The Bubble sort algorithm
def bubbleSort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()


# * The Merge Sort
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        i = 0
        j = 0
        k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


print(items)
mergesort(items)
print(items)


# * The Quicksort
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def quickSort(dataset, first, last):
    if first < last:
        pivotIdx = partition(dataset, first, last)

        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    pivotvalue = datavalues[first]
    lower = first + 1
    upper = last

    done = False
    while not done:
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    return upper


print(items)
quickSort(items, 0, len(items)-1)
print(items)
