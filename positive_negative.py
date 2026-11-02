numbers = [10, -5, 20, -15, 0, 30, -8]

positive = []
negative = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)