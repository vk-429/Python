# name = 'Abhishek'
# for i in name:
#     print(i)
#     if(i == "b"):
#         print("This is something special!")

# colors = ["red","green","blue","yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for k in range(1,20000):
#     print(k+1)

for k in range(1, 12, 3):
    print(k)

person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over keys
for key in person:
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
