# No direct method to do any changes, but we can convert it to list, 
# do changes in th list and then again convert it to tuple

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# We can concatinate 2 tuples
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0,1,2,3,2,31,1,3,2)
# res = tuple1.count(3)
# res = tuple1.count(311) # Error
# res = tuple1.index(3,4,8)
res = len(tuple1)
print('Length of tuple is:', res)