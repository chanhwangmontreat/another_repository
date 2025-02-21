### Taking a user input:

# print(input())
#
# userInput = input("Type in whatever you want to type in!!: ")
#
# print(f"This is the message whatever typed in! {userInput}")
#
# message = input("Tell me something, and I will repeat it back to you: ")


# # print(message)
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
#
# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# # name = input(prompt)
# # print(f"\nHello, {name}!")
#
# ### Can you write a python code comparing whether a user input is greater than 100?
# ### Use input() function to take in a user input.
# ### If so, print a sentence f"This number {} is greater than 100"
### If not, print a sentence f"This number {} is too small!"

# while True:
#     userInput_new = input("Type in a number to compare please! : ")
#     userInput_new = int(userInput_new)
#     if userInput_new >= 100:
#         print(f"This number {userInput_new} is greater than 100!")
#     else:
#         print(f"This number {userInput_new} is too small!")

# # ## Can we debug this example code?
# # age = input("How old are you? ")
# # print(age)
# # print("I am over 18 years old. True or False? , ",int(age) >= 18)
#
#
#
#
#
#
# # age = input("How old are you? ")
# # age = int(age)
# # print(age >= 18)
# # print(age)
#
#
#
# #
# # height = input("How tall are you, in cm? ")
# # height = int(height)
# # if height >= 48:
# #     print("\nYou're tall enough to ride!")
# # else:
# #     print("\nYou'll be able to ride when you're a little older.")
#
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
#
# input("Pause!")

##infinite loop
# current_number = 1
# # must be initialized with a value that results in
# # a true answer or the loop will not execute
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#
## while loop can be stopped if condtion is false.
# # input("pause!")
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
#
#
# ### Break keywords stops any loop which are normally used with
# ### if statements
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")
#

# #### Loop can be used to iterate over all list elements
# # Start with users that need to be verified,
# # and an empty list to hold confirmed users.
# assists = [5, 6, 2, 9]
# confirmed_assists = []
# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.
# while assists:
#     current_assist = assists.pop()
#     print(f"Verifying assists: {current_assist}")
#     confirmed_assists.append(current_assist)
#
# input("pause!")
# # ###while loops with Lists & Dictionaries
# # print(f"Verifying user: {current_user.title()}")
# # confirmed_users.append(current_user)
# # # Display all confirmed users.
# # print("\nThe following users have been confirmed:")
# # for confirmed_user in confirmed_users:
# #     print(confirmed_user.title())
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
#     print("I just removed cat!")
#     print(f"Here are the list elements {pets}")
#     input("Press any key to continue!")
#
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary.
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
