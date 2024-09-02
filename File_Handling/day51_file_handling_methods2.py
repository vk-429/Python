# with open("day51_myfile.txt",'r') as f:
#     print(type(f))
#     # Move to the 10th byte in the file
#     f.seek(10)
#     # Read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

with open('day51_sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('day51_sample.txt', 'r') as f:
  print(f.read())
