shopping_list = [
    "cheese",
    "apples",
    "bread",
    "cheese",
    "milk",
    "eggs",
    "cheese"
]

for item in shopping_list.copy():
    if item == "cheese":
        shopping_list.remove(item)

print(shopping_list)

shopping_list = [
    "cheese",
    "apples",
    "bread",
    "cheese",
    "milk",
    "eggs",
    "cheese"
]

n = shopping_list.count("cheese")

print(f"There are {n} cheese items on the list.")