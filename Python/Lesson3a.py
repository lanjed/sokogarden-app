# if statements
number = -10

# graeter than operator
if number > 0: 
    print('Number is positive')

# less than operator
if number < 0:
    print('Number is negative')

# less than or equal to
num1 = 5
num2 = 2
if num1 <= num2:
    print('num1 is less than or equal to num2')

# greater than or equal to
if num1 >= num2:
    print('num1 is greator or equal to num2')

# equal to
if num2 == 2:
    print('num2 is equal to 2')

# not equal to
if num1 != num2:
    print('num1 and num2 are not equal')


# Logical 'and'
if (num1 < num2) and (num1 > 3):
    print('Both conditions are true (logical and)')

# Logical 'or'
if (num1< num2) or (num1 > 3):
    print('One or both of the conditions is true (logical or)')

# Logical 'not'
if not(num1 < num2):
    print('num1 is not less than num2')
  