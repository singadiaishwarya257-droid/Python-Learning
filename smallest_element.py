numbers = [10, 25, 8, 45, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)