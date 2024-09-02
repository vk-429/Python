tup = (1) # It will give type int
print(type(tup),tup)

tup1 = (1,2,3,4,5,"Vivek",True)
print(type(tup1),tup1)

# Ordered collection
# Immutable, cannot be changed
# Indexing exists
# Both positive indexing and negative indexing
# Slicing can be done, but not in the same variable
# Bound checking available
# Almost same as list, but cannot be changed

if 2 in tup1:
    print("Yes, Present")

tup2 = tup1[1:4]
print(tup2)


country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes