numbers = (10, 20, 30, 20, 40, 10, 50)

unique = ()

for num in numbers:
    if num not in unique:
        unique = unique + (num,)

print("Original Tuple:", numbers)
print("After Removing Duplicates:", unique)