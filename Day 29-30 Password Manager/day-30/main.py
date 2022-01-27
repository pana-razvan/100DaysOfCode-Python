# FileNotFound
with open("a_file.txt") as file:
    file.read()

# KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# IndexError
fruit_list = ["Apple", "Pear", "Banana"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 5)

# Example
# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as KeyError_message:
    print(f"The key {KeyError_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("This is an error that I made up.")
    file.close()
    print("File was closed.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Please enter a valid height.\nHuman height should not be greater than 3 m")

bmi = weight / height ** 2
print(bmi)