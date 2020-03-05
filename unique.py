num = [2,2,1,5,4,6,4,6,7,6]
numbers=(1,2,5)
numbers.index
unique = []
for number in num:
    if number not in unique:
        unique.append(number)
print(unique)