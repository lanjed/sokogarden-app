# python while loops
counter = 1

while counter <=10:
    print(counter)
    # implement counter variable
    counter = counter + 1

# TODO: Always update your counter (or condition) inside the loop!


# Write a program that checks for the real password using while loop
password = ""
correct_password = "secret123"
while password != correct_password:
    password = input("Enter your password")
    if password != correct_password:
        print("Wrong! Try again")

print("Access Granted!")


