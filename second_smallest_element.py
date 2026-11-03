
numbers = [25, 10, 45, 5, 32, 15]

smallest = second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest element:", second_smallest)
