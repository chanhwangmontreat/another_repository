# -*- coding: utf-8 -*-

random_memory_space = 8

print("The content of \"random memory space\" variable is  \"" + str(random_memory_space) + "\"")

addition_result = random_memory_space + 20

print("The content of the variable added by 20 is \"" + str(addition_result) + "\"")

print("The datatype for 'random memory space ' is " + str(type(random_memory_space)))
random_memory_space = 45.33
print("The datatype for 'random memory space ' is " + str(type(random_memory_space)))

random_memory_space = "Any English Text"
print("The datatype for 'random memory space ' is " + str(type(random_memory_space)))

print("The content of the variable added by 20 is " + str(addition_result))

print(addition_result)
## can you make a variable "your name"
# and then assign it an integer of 15
## add the variable division by 3 and store the output result into
# a new variable "division output"





aString_Example = "inchan"
print("I just picked up An element in a list '" + aString_Example[-2] + "'")
##A list is a collection of ordered elements that can hold multiple values in a single variable.
#Lists are widely used in programming and data structures due to their flexibility and ease of manipulation.
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'Dragon']
print(bicycles)

print("If you use title() then 1st char is capitalized " +bicycles[0].title())

## 2nd eleement
print(bicycles[1])
print(bicycles[3])
## Can you display 5th element?
print(bicycles[4])



#it allows variables or calculations directly inside a string.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# can you write a calculation inside the string?
country_of_birth = ["USA","Japan","Korea"]
# message = "My country of Birth is " + country_of_birth[1]
message = f'My country of Birth is {country_of_birth[1]}'
print(message)

print("'My country of Birth is " + country_of_birth[1])

### replace an element with another one
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[1] = "Ford"

print(motorcycles)
## can you replace 3rd element with "Subaru'?
motorcycles[2] = "Subaru"

print(motorcycles)
## Add element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print("List element was added")
print(motorcycles)
## Can you add another element "RAM"?
motorcycles.append("RAM")
print("'RAM' element was added")
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print("New list 'ducati' was added in the beginning !"  + str(motorcycles))
## Can you insert an element "Lamborghini" in the 3rd index?
motorcycles.insert(2, "Lamborghini")

print(f"I just added a new element in the 3rd index \"{motorcycles[2]}\"")




### removing an element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"Source list is : \"{motorcycles}\"")
del motorcycles[0]
print(f"after the 1st element was removed: \"{motorcycles}\"")

## can you remove the last element?
del motorcycles[-1]
print(f"after the last element was removed: \"{motorcycles}\"")
### pops out the last element and return the last element
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

### removing an element by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

### can you remove "yamaha" element?
motorcycles.remove('yamaha')
print(f"\n Yes~ I removed 'Yamaha!!'  Here is the new list '{motorcycles}' ")


#Sorted data allows for faster searching algorithms, such as Binary Search,
#which operates in O(log⁡n)O(logn) time compared to Linear Search (O(n)O(n))
## using an embedded sort() feature of a list data type.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
## In Reverse:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

### Sort() function also returns a sorted list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)