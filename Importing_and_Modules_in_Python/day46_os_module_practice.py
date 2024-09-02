import os

# Open the file in read-only mode
f = os.open("day46_myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)
print(contents)
# Close the file
os.close(f)

# Open the file in write-only mode
f = os.open("day46_myfile.txt", os.O_WRONLY)
# Write to the file
os.write(f, b"Hello, world!")
# Close the file
os.close(f)