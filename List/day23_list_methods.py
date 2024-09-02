l = [8,10,11,3,5,1,2,4,6,1,2,3,3]
print(l)

# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(3))

# m = l # Here it being shallow copy
#  If we'll change m, they will also appear in l
# so use
# m = l.copy()
# m[0] = 0
# l.insert(1,899)
m = [900,1000,1100]
l.extend(m)
print(l)

k = l + m
print(k)
