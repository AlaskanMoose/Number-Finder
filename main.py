import time
from itertools import permutations, repeat


def bestCase(list1, list2):
    resultList = []
    target = 6
    normal_set = set()

    for num in list1:
        normal_set.add(num)

    for num in list2:
        factor = target / num
        if factor in normal_set:
            resultList.append(int(factor))
            resultList.append(num)
    print(resultList)


def badCase(list1, list2):
    resultList = []
    target = 6

    for numFromList1 in list1:
        for numFromList2 in list2:
            if numFromList1 * numFromList2 == target and len(resultList) < 2:
                resultList.append(numFromList1)
                resultList.append(numFromList2)
    print(resultList)


def worstCase(list1, list2):
    target = 6
    resultList = []
    perm = [list(zip(list1, p)) for p in permutations(list2)]

    for tuple in perm:
        for t in tuple:
            if t[0] * t[1] == target and len(resultList) < 2:
                resultList.append(t[0])
                resultList.append(t[1])
    print(resultList)


def initializeBigList():
    arr = []
    for i in range(9):
        arr.append(1)
    return arr


if __name__ == "__main__":
    list1 = initializeBigList()
    list2 = initializeBigList()
    list2.append(6)

    print("When list sizes are 9 elements")

    start_time = time.time()
    bestCase(list1, list2)
    print("---bestcase took %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    badCase(list1, list2)
    print("---badcase took %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    worstCase(list1, list2)
    print("---worstcast took %s seconds ---" % (time.time() - start_time))
