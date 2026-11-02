numbers = [0, 10, 0, 20, 30, 0, 40]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

zeros = numbers.count(0)

result.extend([0] * zeros)

print("Updated list:", result)