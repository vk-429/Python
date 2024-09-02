dic = {
    "Harry":"Human being",
    "Spoon":"Object"
}

print(dic)
print(dic['Harry'])

# Ordered collection of key value pair

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name']) # If key doesn't exist it will throw an error
print(info.get('eligiblee')) # If key not found, print None
print(info.values())
print(info.keys())

for key in info.keys():
    print(key,":",info[key])

print(info.items())
for key,value in info.items():
    print(key,":",value)