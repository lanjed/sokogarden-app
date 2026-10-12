# exception errors (Logical bugs)

amount = 10000

# a = amount / 0
# print(a)

try:
    a = amount/0
    print(a)
except Exception as error:
    print("Exception caught", error)

    
