import math

print(math.ceil(4.2))
print(math.floor(2.9))

is_hot = True
is_cold=True
if is_hot:
    print("It's hot enjoy your day")
    print("Drint lots of water")
elif(is_cold):
    print("Wear heavy clothing")
else:
    print("You are safe")

if is_hot and is_hot:
    print("awkward")

temp = 35
if temp>25:
    print("Its hot out there")
else:
    print("its cold")