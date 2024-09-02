# f = open('day49_myfile2.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         # print(line,type(line))
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in math is : {m1}")
#     print(f"Marks of student {i} in english is : {m2}")
#     print(f"Marks of student {i} in science is : {m3}")
#     print(line)

f = open('day49_myfile3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()