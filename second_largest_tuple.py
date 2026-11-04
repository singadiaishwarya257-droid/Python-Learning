numbers = (10, 25, 5, 40, 30)

unique = set(numbers)
unique.remove(max(unique))

print("Second largest:", max(unique))