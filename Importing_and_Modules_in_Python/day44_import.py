'''In summary, the import statement in Python allows you 
to access the functions and variables defined in a module 
from within your current script. You can import the entire 
module, specific functions or variables, or use the * wildcard 
to import everything. You can also use the as keyword to 
rename a module, and the dir function to view the contents of 
a module.'''

# import pandas
# pandas.read_csv()

# from math import sqrt,pi
# from math import *

# When module name is big or we want to make its name more explanatory
# we can use as keyword to do rename it according to our requirement

# from math import pi, sqrt as s
# result = s(9) * pi
# print(result)

# import math

# print(dir(math))
# print(math.nan,type(math.nan))

# from day44_import1 import welcome,harry
# from day44_import1 import *
import day44_import1 as hr
hr.welcome()
print(hr.harry)