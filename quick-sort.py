#!!!!!! QuickSort !!!!!!!! average case- O(log n)
# [5,4,8,1,9,2]
# pivot val: 2
# [5,4,8,1,9] 
# pivot 2: lower and higher
# ............1. 2 .5.4.8.9.
# 1,2,5,4,8,9
# pivot: 9
# lower.......... pivot ...........higher
import random

list = []
for i in range(10):
    list.append(random.randint(1,20))

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
    list_lower = []
    list_higher = []

    for i in list:
        if i > pivot:
            list_higher.append(i)
        else:
            list_lower.append(i)

    return quick_sort(list_lower) + [pivot] + quick_sort(list_higher)

print(list)
print(quick_sort(list))
