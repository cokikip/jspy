New = ["Collins","Kiplagat", "Kiprono", "Evans","Omondi","Otieno"]
for less in New:
    print(less+"\n")
print(New[5:])

num = [12,11,15,11,18,19,13]
num.append(25)
num.insert(1, 80)
print(num.count(11))
num.sort()
num.reverse()

print(num)
num.pop()
print(num)
max = num[0]
for n in num:
    if n>max:
        max = n
print(max)
num.clear()
print(num)