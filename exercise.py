name = input("Enter your name: ")
print(type(len(name)))
# its not a must to  convert to integer sicnce its already in integer
i = int(len(name))
print(i)
if i < 3:
    print("Name must be atleast 3 characters")
elif i > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name is good")
