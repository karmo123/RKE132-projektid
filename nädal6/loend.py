shopping_list = ["apples", "bread", "milk", "eggs"]

# len()
print(f"We have {len(shopping_list)} items on the list.")

# append()
shopping_list.append(["flour", "sugar", "baking powder"])

print(f"We have {len(shopping_list)} items on the list.")

print(shopping_list)

for item in shopping_list:
    print(item)



shopping_list = ["apples", "bread", "milk", "eggs"]

shopping_list.extend(["flour", "sugar", "baking powder"])

print(f"We have {len(shopping_list)} items on the list.")

print(shopping_list)

for item in shopping_list:
    print(item)