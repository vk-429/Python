s1 = {1,2,5,6}
s2 = {3,6,7}

# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.union(cities2)
# cities3 = cities.intersection(cities2)
# print(cities3)
# cities.intersection_update(cities2)
# print(cities)

# cities4 = cities.symmetric_difference(cities2)
# print(cities4)
# cities.symmetric_difference_update(cities2)
# print(cities)
# cities5 = cities.difference(cities2)
# print(cities5)
# cities.difference_update(cities2)
# print(cities)

# print(cities.isdisjoint(cities2))
# cities3 = {"Tokyo","Madrid","Delhi"}
# print(cities.issuperset(cities3))
# print(cities3.issubset(cities))

# cities.add("Helsinki")
# cities.remove("Tokyo")
# cities.discard("Berlin")
# Remove throws an error if element is not present
# while discard doesn't throws an error
# print(cities.pop()) # deletes any random element
# print(cities)
# cities.clear()
# print(cities)

# del cities
# print(cities) # can't use after del

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


