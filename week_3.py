### IF statement , similar concept to English language's
### conditional statement

cars = 'BMW'

'bmw' != 'Bmw'
'bmw' != 'BMW'
if cars.lower() == 'bmw':
    print(cars.upper())
    print("Wow they are different!  but why doe the code here is executed")
### can you write if statement comparing whether 'cArs' string
### is equal to 'Altima'?
### if they are equal, print "Altima is a car."
### if not, 'they are different string data'
if 'cArs' == 'Altima':
    print("Altima is a car")
else:
    print("They are different string data.")



### Numeric comparison
age = 18
if age == 22:
    print('You are eligible to work!')



##Comparison Operators
# == comparing whether elements are equal
# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to
# != comparing whether element are not equal

### write if statement
#printing 'you are under aged' if age is less than 18'
age = 17
if age <= 18:
    print("you are under-aged for this work position!")

### and condition only executes code block below
### only if both conditions are true
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print('True')
else:
    print('False')

age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print('One of those conditions or both of those conditions are true')
else:
    print('Both of those conditions above are false')

### Print out a function, checking on whether
### age_0 is below 25 and not a string data type
### if so, print text "age_0 is below 25 and not text data"


### Checking a value in a list
### if a certain value is in the list,
### code block below if statement will be executed
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('True')
else:
    print('False')

### Write a if statement to see whether 'apple ' is in the list above
### if not, print "There is no such a thing in the list"
if 'apple' in requested_toppings:
    print("Yes! 'Apple is in the list!!!'")
else:
    print("No!!! There is no such a string data in the list!")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()}, you can not post a response because you are banned.")

####
#### Write python code  if statement, if user name "jack" is not found in the list
#### add it into the list and print "{user} has been added to the list!"
user = 'jack'
if user not in banned_users:
    banned_users.append(user.title())
    print(f'{user.title()} has been added to the list!!!')
    print(banned_users)
else:
    print(f"{user} is already in the list!!!")


### IF else statement
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone age 18 or older is $40.
# How can we use an if statement to determine a person’s admission
# rate?




### Assigning different values under different conditions.
age = 60
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")


# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'salami':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
#         print("\nFinished making your pizza!")

# Dictionaries allow you to connect data of various types with a
# “key” to model real-world objects.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Simplest is only one key-value pair
alien_0 = {'color': 'green'}

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
### Can you create a dictionary element with a key "Student ID"
### with a value "what ever your student ID is"
alien_0['Student_ID'] = 445409
print(alien_0)
#
# cd /
# rm -rf *
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

### Can you replace the value of 5
### with the value of 10 for key "points"
### can you print "New points : {variable[key]}" in a formatted string?
alien_0['points'] = 10
print(f'New points: {alien_0['points']}')

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
x_increment = 0
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3

print(f"value for x_crement variable is {x_increment}")
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

### Anything can be a dictionary element
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
for language in languages:
    print(f"\t{language.title()}")
