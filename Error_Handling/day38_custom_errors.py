a  = input("Enter any value betwwen 5 an 9: ")

if(a != 'quit'):
   if int(a)<5 or int(a)>9:
    raise ValueError("Value should be between 5 an 9")
   
print(a)

# Defining Custom Exceptions

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...
# except CustomError:
#   # code...

