
##A list is a collection of ordered elements that can hold multiple values in a single variable.
#Lists are widely used in programming and data structures due to their flexibility and ease of manipulation.
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'Dragon']
print(bicycles)

print(bicycles[0].title())

## 2nd eleement
print(bicycles[1])
print(bicycles[3])
## Can you display 5th element?




#it allows variables or calculations directly inside a string.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# can you write a calculation inside the string?

### replace an element with another one
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

## can you replace 3rd element with "Ford'?


## Add element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
## Can you add another element "RAM"?

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
## Can you insert an element "Lamborghini" in the 3rd index?


### removing an element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

## can you remove the last element?


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