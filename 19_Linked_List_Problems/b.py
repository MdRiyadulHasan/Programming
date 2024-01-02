def mergeKLists(lists) -> None:
    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if lists else None

def mergeTwoLists(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result
lists = [[5, 6, 7], [2, 4, 5], [3, 8, 9], [7, 10, 12], [9, 11, 15]]
result = mergeKLists(lists)
print(result)