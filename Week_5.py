# Named blocks of code designed to do a specific job.
# Call a function to run the code.
# Functions are modular and can be called repeatedly each time
# # you need that specific job. More efficient
# a = 12
# b = "twenty five"
#
# print(a, b)
#
# def linear_line_function(slope, x_var, y_intercept):
#     y = slope * x_var + y_intercept
#     return y
#
# print()

def greet_user(): #function definition header
# Display a simple greeting.""“ # function body
    print("Hello!") # function body

greet_user() #Calling a function to run


### Can you write your own function displaying your name?
###
# def MyName_Display():
#     print("I am Inchan Hwang!")


def greet_user(username):
# """Display a simple greeting."""
    print(f"Hello, {str(username).title()}!")

greet_user('jesse')


# # def greet_user(username):
# # • username is a parameter that the function expects to be passed.
# # • It can be passed as a variable or a value.
# # • When calling the function, what is in () is called an argument
#

def describe_pet(animal_type, pet_name, gender):
    #two parameters
# """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
    print(f"This little baby is a {gender}.")


### Can you call a user defined function above
## while specifying function parameters
## so that Even if function argument order is reversed,
## the message display will look normal



# describe_pet('hamster', 'harry')
#                         # '#two arguments

def describe_pet(animal_type, pet_name): #two parameters
# """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') #two arguments in a function call
describe_pet('dog', 'willie')

#
# def describe_pet(animal_type, pet_name): #two parameters
# # """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
#
# describe_pet('harry', 'hamster') #two arguments in a function call
# describe_pet('willie','dog')
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')
#
#
# def describe_pet(pet_name, animal_type='dog'): #two parameters
# # """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster', pet_name='harry')
# # '#order
# # doesn’t matter
# describe_pet(pet_name='willie')
#

def describe_pet(pet_name, animal_type='dog'): #two parameters
# """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


def describe_pet(pet_name='Mike', animal_type='dog'): #two parameters
# """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

### Can you add modification to the code above
### pet_name has a default string value "Mike"
### Can you call the user defiend function
### without placing any inputs?



## You can use other python syntax in Python functions.
## This function returns formatted string.
def get_formatted_name(first_name, last_name):
# """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def game_changer(old_sentence):
    new_sentence = old_sentence.replace("ugly", "pretty").replace("an", "a")
    return new_sentence
#
# musician = get_formatted_name('jimi', 'hendrix') #return value to
# # variable musician
# print(musician)

## can you write a python function replacing substring "Ugly"
## with "Pretty"? This function takes in string variable"
## "You are an ugly student at Montreat College"

#
def get_formatted_name(first_name, last_name, middle_name=''):
# """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()
#
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

### Can we add modification to the function above ?
### can you add nickname parameter to the function
### Function must include the nickname in the output
##3 if there is any value in the nickname parameter.


def get_formatted_name(first_name, last_name):
# """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') #return value to
# variable musician
print(musician)

###Making argument optional!
def get_formatted_name(first_name, last_name, middle_name=''):
# """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

### Can you add optional french name to the function?
###

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

### Dictionary returned
def build_person(first_name, last_name):
# """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

### Can you add parents' names to the function parameters
### and add them to the dictionary too?

def get_formatted_name(first_name, last_name):
# """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    get_formatted_name(f_name, l_name)


## can you make another function formatting your
## friends' nickname while capitalizing all of them?


