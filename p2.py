# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))
# print(fruits.count('tangerine'))
# print(fruits.index('banana'))
# fruits.reverse()
# print(fruits)
# fruits.append('grape')
# print(fruits)
# fruits.sort()
# print(fruits)
# print(fruits.pop())
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# print(stack.pop())
# print(stack)

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# print(queue)           # Terry arrives
# queue.append("Graham")
# print(queue)          # Graham arrives
# print(queue.popleft())                 # The first to arrive now leaves
# print(queue.popleft())                 # The second to arrive now leaves
# print(queue)                

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print([[row[i] for row in matrix] for i in range(4)])

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# empty = ()
# singleton = 'hello',    # <-- note trailing comma
# print(len(empty))
# print(len(singleton))
# print(singleton)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)     
# print('orange' in basket)
# print('crabgrass' in basket)

# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)
# print(tel['jack'])
# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# print(list(tel))
# print(sorted(tel))
# print('guido' in tel)
# print('jack' not in tel)

# # import fibo
# # print(fibo.fib(1000))

# # from fibo import fib, fib2
# # fib(500)

# s = 'Hello, world.'
# print(str(s))

# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)

# table = {'sjoerd' : 4127, 'jack' : 4098, 'Dacb' : 7678}
# for name, phone in table.items():
#     print('{name : 10} ==> {phone :10d}')
    
# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')

# animals = 'eels'
# print(f'My hovercraft is full of {animals}.')

# bugs = 'roaches'
# count = 13
# area = 'living room'
# print(f'Debugging {bugs=} {count=} {area=}')

# with open('workfile', 'r', encoding="utf-8") as f:
#     read_data = f.read()
# f.close()


# # Reading from a file
# try:
#     with open('abc.txt', 'r') as f:
#         content = f.read()
#         print("File Content:")
#         print(content)
# except FileNotFoundError:
#     print("The file does not exist.")
# except IOError:
#     print("An error occurred while reading the file.")

# # Writing to a file
# content_to_write = "This is some new content added to the file.\n"

# with open('abc.txt', 'a') as f:  # 'a' mode is for appending
#     f.write(content_to_write)
#     print("Content has been written to the file.")
    
# with open('abc.txt','w') as f:
#     f.write('This is a test\n')
#     a= f.read()
#     print(a)
    
# try:
#     with open('abc.txt', 'rb+') as f:
#         content = f.write(b'0123456789cdefd')
#         print("File Content:")
#         print(content)
# except FileNotFoundError:
#     print("The file does not exist.")
# except IOError:
#     print("An error occurred while reading the file.")

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
        
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                         #  but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)
    
# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise    
   
# def this_fails():
#     x = 1/0

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)


# try:
    
#     result = 10 / 0
# except ZeroDivisionError as e:
#         print(f"Error occurred: {e}")
# else:
#         print("Operation was successful!")
# finally:
#         print("Cleaning up...")


# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     else:
#         print(f"Result: {result}")
#     finally:
#         print("Exiting the function.")
# divide_numbers(10, 2)
# divide_numbers(10, 0)
   
# try:
#     num = int(input("Enter a number:"))
#     result =10/num
# except ZeroDivisionError:
#     print("error: Invalid input!pleae enter a number.")
# except Exception as e:
#     print("An unexpected error occurred:{e}")
# else:
#     print(f"Result:{result}")
# finally:
#     print("Operation completed.")
    
# def check_positive_number(num):
#     if num <= 0:
#         raise ValueError("The number must be positive!")
#     else:
#         print(f"The number is: {num}")
# try:
#     check_positive_number(-5)
# except ValueError as e:
#     print(f"Error: {e}")    
    
# try:
#     num = 10/0
# except ArithmeticError:
#     print("An airthmetic error occurred.")
# except ZeroDivisionError:
#     print("Division by zero error.")
    
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')
    
# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

# class Complex:
#     def __init__(self,realpart,imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r , x.i)

# class Dog:
#     tricks = []
#     def __init__(self,name):
#         self.name = name
#     def add_trick(self,trick):
#         self.tricks.append(trick)
#     d = Dog('fido')
#     e = Dog ('buddy')
#     d.add_trick('roll over')
#     e.add_trick('play dead')
# print(d.tricks)

# from dataclasses import dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int
# john = Employee()
# john.dept


# import threading
# import time
# def print_number():
#     for i in range(5):
#         time.sleep(1)
#         print(i)
        
# thread1 = threading.Thread(target=print_number)
# thread2 = threading.Thread(target=print_number)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Both threads have finished execution.")

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))