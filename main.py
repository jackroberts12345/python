# Create function called greetings()
# First parameter: first name
# Second parameter: last name
# Last parameter: age

# greetings('Samir', 'Chahine', 21)
# "Hello Samir Chahine, you are 21 years old"def fname(arg):


def greetings(first_name):
    print("Hello " + first_name)

first_names = ['samir', 'sam', 'daniel', 'rachel']

for index in range(0, 4):
    greetings(first_names[index])
