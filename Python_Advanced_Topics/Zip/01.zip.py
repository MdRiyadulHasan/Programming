list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['!', '@', '#']
zipped = zip(list1, list2, list3)
for item in zipped:
    print(item)