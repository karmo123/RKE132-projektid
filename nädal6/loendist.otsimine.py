shopping_list = [
    "cheese",
    "apples",
    "bread",
    "cheese",
    "milk",
    "eggs",
    "cheese"
]

found = False

for item in shopping_list:
    if item == "soy milk":
        found = True
        break

if found:
    print("Soy milk is already on the list.")
else:
    print("There is no soy milk on the list.")