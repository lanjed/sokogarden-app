# for loops with sequences
languages = ['English','Japanese','Kiswahili','Chinese','spanish','French','Italian']

for language in languages:
    print(language)
    for letter in language:
        print(letter)

# create a tuple of colors and list them and their characters
colors = ('Brown','Red','White','Black','Purple')

for color in colors:
    print(color)
    for letter in color:
        print(letter)

# create a mathematical table of 5 (1..10)
number = 5
for val in range(1,11):
    result = number * val
    print(f"{number} x {val} = {result}")