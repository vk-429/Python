class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()

# print(a.__name) # Can't be accessed directly
print(a._Employee__name) # Can be accessed directly

print(a.__dir__())

# class Student: 
#     def __init__(self, age, name): 
#         self.__age = age      # An indication of private variable
        
#         def __funName(self):  # An indication of private function
#             self.y = 34
#             print(self.y)

# class Subject(Student):
#     pass

# obj = Student(21,"Harry")
# obj1 = Subject

# # calling by object of class Student
# print(obj.__age)
# print(obj.__funName())

# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())