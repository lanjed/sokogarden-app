# functions with parameters
def greet(name):
    """testing docstring implementation"""
    print('Hi',name)

greet("Jeddy") # the value is called an argument

# create a simple calculator using parameters
def addition(num1, num2):
    sum = num1 + num2
    print("The sum is ", sum)

addition(10,20)

def multiplication(num1,num2,num3):
    mult = num1 * num2 * num3
    print("The multiplicaton is", mult)

def multiplication(num1):
    mult = num1 * num1
    print('square multiplication is', mult)

def multiplication(num1 = 10):
    mult = num1 * num1
    print("Default parameter multiplication", mult)

# multiplication(54, 23,12)
multiplication(67)
# multiplication()