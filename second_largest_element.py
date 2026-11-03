
numbers = [10, 25, 8, 45, 32, 15]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element:", second_largest)
