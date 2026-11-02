numbers = [1, 2, 4, 6, 7, 9]

missing = []

for num in range(1, 10):
    if num not in numbers:
        missing.append(num)

print("Missing numbers:", missing)