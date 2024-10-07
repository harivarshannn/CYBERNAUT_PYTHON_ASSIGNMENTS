num_items = int(input("Enter the number of items you want in the lists: "))

keys = []
for i in range(num_items):
    key = input(f"Enter key {i + 1}: ")
    keys.append(key)

values = []
for i in range(num_items):
    value = input(f"Enter value {i + 1}: ")
    values.append(value)

dictionary = dict(zip(keys, values))
print(dictionary)
