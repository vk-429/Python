# abs()
print(abs(-5))  # Output: 5

# all()
print(all([True, True, False]))  # Output: False

# any()
print(any([False, False, True]))  # Output: True

# ascii()
print(ascii('ñ'))  # Output: '\xf1'

# bin()
print(bin(10))  # Output: '0b1010'

# bool()
print(bool(0))  # Output: False

# bytearray()
ba = bytearray("hello", "utf-8")
print(ba)  # Output: bytearray(b'hello')

# bytes()
b = bytes("hello", "utf-8")
print(b)  # Output: b'hello'

# callable()
def foo():
    pass
print(callable(foo))  # Output: True

# chr()
print(chr(97))  # Output: 'a'

# classmethod()
class MyClass:
    @classmethod
    def hello(cls):
        return "Hello"
print(MyClass.hello())  # Output: 'Hello'

# compile()
code = "print('Hello, World!')"
compiled_code = compile(code, 'string', 'exec')
exec(compiled_code)  # Output: Hello, World!

# complex()
z = complex(1, 2)
print(z)  # Output: (1+2j)

# delattr()
class MyClass:
    def __init__(self):
        self.x = 10
obj = MyClass()
delattr(obj, 'x')

# dict()
d = dict(a=1, b=2)
print(d)  # Output: {'a': 1, 'b': 2}

# dir()
print(dir([]))  # Output: List of attributes and methods of a list object

# divmod()
print(divmod(10, 3))  # Output: (3, 1)

# enumerate()
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)
# Output:
# 0 a
# 1 b
# 2 c

# eval()
print(eval('2 + 2'))  # Output: 4

# exec()
code = "for i in range(3): print(i)"
exec(code)
# Output:
# 0
# 1
# 2

# filter()
numbers = [1, 2, 3, 4]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# float()
print(float(3))  # Output: 3.0

# format()
print(format(3.14159, '.2f'))  # Output: '3.14'

# frozenset()
fs = frozenset([1, 2, 3])
print(fs)  # Output: frozenset({1, 2, 3})

# getattr()
class MyClass:
    x = 10
obj = MyClass()
print(getattr(obj, 'x'))  # Output: 10

# globals()
print(globals())  # Output: Dictionary of global variables

# hasattr()
class MyClass:
    x = 10
obj = MyClass()
print(hasattr(obj, 'x'))  # Output: True

# hash()
print(hash('test'))  # Output: Hash value of the string 'test'

# help()
help(print)  # Output: Help information for the print function

# hex()
print(hex(255))  # Output: '0xff'

# id()
a = 10
print(id(a))  # Output: Unique identifier for the object 'a'

# input()
# Uncomment to use
# name = input("Enter your name: ")
# print(name)

# int()
print(int('10'))  # Output: 10

# isinstance()
print(isinstance(10, int))  # Output: True

# issubclass()
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))  # Output: True

# iter()
my_list = [1, 2, 3]
it = iter(my_list)
print(next(it))  # Output: 1

# len()
print(len('hello'))  # Output: 5

# list()
print(list('hello'))  # Output: ['h', 'e', 'l', 'l', 'o']

# locals()
def local_demo():
    a = 10
    print(locals())
local_demo()  # Output: {'a': 10}

# map()
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16]

# max()
print(max([1, 2, 3]))  # Output: 3

# memoryview()
mv = memoryview(b"hello")
print(mv[1])  # Output: 101 (ASCII code of 'e')

# min()
print(min([1, 2, 3]))  # Output: 1

# next()
it = iter([1, 2, 3])
print(next(it))  # Output: 1

# object()
obj = object()
print(obj)  # Output: <object object at ...>

# oct()
print(oct(8))  # Output: '0o10'

# open()
with open('example.txt', 'w') as f:
    f.write('Hello, World!')

# ord()
print(ord('a'))  # Output: 97

# pow()
print(pow(2, 3))  # Output: 8

# print()
print('Hello, World!')  # Output: Hello, World!

# property()
class MyClass:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

obj = MyClass()
obj.x = 5
print(obj.x)  # Output: 5

# range()
for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2

# repr()
print(repr('hello\n'))  # Output: "'hello\\n'"

# reversed()
for i in reversed([1, 2, 3]):
    print(i)
# Output:
# 3
# 2
# 1

# round()
print(round(3.14159, 2))  # Output: 3.14

# set()
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# setattr()
class MyClass:
    pass
obj = MyClass()
setattr(obj, 'x', 10)
print(obj.x)  # Output: 10

# slice()
s = slice(1, 5, 2)
print([1, 2, 3, 4, 5][s])  # Output: [2, 4]

# sorted()
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# staticmethod()
class MyClass:
    @staticmethod
    def hello():
        return "Hello"
print(MyClass.hello())  # Output: 'Hello'

# str()
print(str(10))  # Output: '10'

# sum()
print(sum([1, 2, 3]))  # Output: 6

# super()
class A:
    def hello(self):
        return "Hello from A"
class B(A):
    def hello(self):
        return super().hello() + " and B"
print(B().hello())  # Output: 'Hello from A and B'

# tuple()
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

# type()
print(type(10))  # Output: <class 'int'>

# vars()
class MyClass:
    def __init__(self):
        self.x = 10
obj = MyClass()
print(vars(obj))  # Output: {'x': 10}

# zip()
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# __import__()
math = __import__('math')
print(math.sqrt(4))  # Output: 2.0
