f = open('day49_myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# f2 = open('day49_myfile2.txt','w')
# f2.close()

f3 = open('day49_myfile.txt','a')
f3.write('\nHey i am vivek')
f3.close()

f4 = open('day49_myfile.txt', 'r')
text = f4.read()
print(text)
f4.close()

# automatically close the file
with open('day49_myfile.txt', 'a') as f5:
    f5.write("Hey, I am inside with")


# read (r): This mode opens the file for reading only 
# and gives an error if the file does not exist. 
# This is the default mode if no mode is passed as 
# a parameter.

# write (w): This mode opens the file for writing 
# only and creates a new file if the file does not 
# exist.

# append (a): This mode opens the file for appending 
# only and creates a new file if the file does not 
# exist.

# create (x): This mode creates a file and gives an 
# error if the file already exists.

# text (t): Apart from these modes we also need to 
# specify how the file must be handled. t mode is 
# used to handle text files. t refers to the text 
# mode. There is no difference between r and rt or w 
# and wt since text mode is the default. 
# The default mode is 'r' (open for reading text, 
# synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).

