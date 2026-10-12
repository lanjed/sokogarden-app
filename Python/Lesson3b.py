# if...else statements
number = -10

if number > 0:
    print('Positive number')
else:
    print('Negative number')

# greater than or equal to
num1 = 10
num2 = 20
if num1 >= num2:
    print('num1 is greater than num2')
else:
    print('num2 is greater than num1')

# equal to
if (num1-num2) == number:
    print('The result is equal')
else:
    print('The result is not equal')

# logical 'and'
if (num2 < num1) and (num1 >= 10):
    print('The result of the two conditions is true')
else:
    print('The result of the two conditions is not true')

# logical 'not'
if not(num1 > 10):
    print('num1 is greater than 10')
else:
    print('num1 is graeter than 10')