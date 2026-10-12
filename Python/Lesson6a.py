# implementing modules

def addNumbers(num1, num2):
    sum= num1 + num2
    print("The sum is", sum)

def subtractNumbers(num1, num2):
    if(num1 > num2):
        sub = num1 - num2
        print("The subtraction is", sub)
    elif(num2 > num1):
        sub = num2 - num1
        print("The subtraction is", sub)

def modulus(num1, num2):
    modul = num1 % num2
    print("The modulus is", modul)


def division(num1, num2):
    div = num1 / num2
    print("The division is", div)
