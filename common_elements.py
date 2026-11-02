list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)