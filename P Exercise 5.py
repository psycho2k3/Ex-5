# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits

fruit_list = ["Strawberry", "Coconut", "Pineapple", "Watermelon", "Litchi"]

# TODO: Add a fruit to the end of the list

fruit_list.append("Blackberry")

# TODO: Insert a fruit at the beginning of the list

fruit_list.insert(0,"Naartjie")

# TODO: Remove a fruit from the list

fruit_list.remove("Watermelon")

# TODO: Print the modified list

# print(fruit_list)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5

numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared

squared_numbers = [int(num) **2 for num in numbers]
print(squared_numbers)

# TODO: Find the sum and average of the original numbers

int_number = [int(num) for num in numbers]
total_sum = sum(int_number)
avg = total_sum / len(int_number)

# TODO: Print the results

print("Sum: ", total_sum)
print("Average: ", avg)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals

countries_and_capitals = {
    "South Africa": "Pretoria",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
}

# TODO: Add a new country-capital pair

countries_and_capitals["Australia"] = "Canberra"

# TODO: Update the capital of an existing country

countries_and_capitals.update({"South Africa": "Cape Town"})

# TODO: Remove a country-capital pair

countries_and_capitals.pop("Brazil")

# TODO: Print the modified dictionary
print(countries_and_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors

fruit_colours ={
    "orange": "orange",
    "grape": "purple",
    "lemon": "yellow",
    "cranberry": "red"
}

# TODO: Print all the fruits (keys)

print("Fruits:")
for fruit in fruit_colours.keys():
    print(fruit)

# TODO: Print all the colors (values)

print("\nColors:")
for color in fruit_colours.values():
    print(color)

# TODO: Print each fruit and its color

print("Fruits and their colours:")
for fruit, color in fruit_colours.items():
    print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color

fruit_to_check = "Banana"
if fruit_to_check in fruit_colours:
    print(f"\nThe color of {fruit_to_check} is {fruit_colours[fruit_to_check]}.")
else:
    print(f"\n{fruit_to_check} is not in the dictionary.")