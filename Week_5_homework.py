def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
### ** user_info parameter is used when you dont know
### how many arguments you need to place values into parameters
### You use ** signs in
### tp accept an arbitrary number of keyword arguments (i.e., named arguments)
user_profile = build_profile('albert','einstain',
                             location="princeton",
                             field="physics")
### location and field arguments are passed into function
### They are stored into a variable in the form of dictionary
print(user_profile)

import make_pizza_func

make_pizza_func.make_pizza(3, 'corn','onion','sausage'
                           ,'pineapple')

from make_pizza_func import make_pizza
make_pizza(3, 'corn','onion','sausage'
                           ,'pineapple')