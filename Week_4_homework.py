# # user_input = ""
# while user_input != 'quit':
#     user_input = input("type in a pizza topping of your choice : ")
#     if user_input == 'quit':
#         print("This software was finished!")
#         break
#     print(f"You will add '{user_input}' to your pizza! ")
age = 0
ticket_price = 0
iteration_limit = 0
while True:
    print(f"You are in the {iteration_limit + 1}th iteration ")
    age = input("Type in your age : ")
    age = int(age)
    if age < 3:
        ticket_price = 0
    elif age >= 3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"The cost of ticket price for you is ${ticket_price}")
    iteration_limit = iteration_limit + 1
    if iteration_limit >= 5:
        print(f"This software is terminated after {iteration_limit+1} iteration(s)")
        break

































# # Topping_List = []
# # user_input = ""
# # while user_input != 'quit':
# #     user_input = input("type in a pizza topping of your choice :")
# #     if user_input == 'quit':
# #         break
# #     print(f"You will add {user_input} topping to their pizza!")
#
# ###
# age = 0
# ticket_price = 0
#
#
# while True:
#     age = input("Type in your age!")
#     if age == 'quit':
#         print("This software stops working now.")
#         break
#     age = int(age)
#
#     if age < 3:
#         ticket_price = 0
#     elif age >= 3 and age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 12
#
#     print(f"Your ticket price is ${ticket_price}")
#
