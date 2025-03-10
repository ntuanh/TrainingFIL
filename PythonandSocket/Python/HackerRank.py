def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant method to find the root of a function.

    Parameters:
    func (function): The function for which we are trying to find the root.
    x0 (float): Initial guess 1.
    x1 (float): Initial guess 2.
    tol (float): Tolerance for convergence (difference between successive approximations).
    max_iter (int): Maximum number of iterations.

    Returns:
    float: The estimated root.
    int: Number of iterations performed.
    """
    for i in range(max_iter):
        f0 = func(x0)
        f1 = func(x1)

        # Calculate the difference (delta) between x1 and x0
        delta = abs(x1 - x0)

        # Print delta for each iteration
        print(f"Iteration {i + 1}: Delta = {delta:.10f}")

        # Check if the difference between x1 and x0 is within the tolerance
        if delta < tol:
            return x1, i

        # Calculate the new approximation
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        # Update the values
        x0, x1 = x1, x2

    return x1, max_iter


# Define the function
def f(x):
    return x ** 3 + x - 1000


# Initial guesses
x0 = 9.0
x1 = 10.0

# Call the secant method
root, iterations = secant_method(f, x0, x1, tol=1e-6)

# Output the result with 6 digits after the decimal
print(f"\nRoot: {root:.6f}")  # Display 6 decimal places
print(f"Iterations: {iterations}")



""" numpy libraly"""
# import numpy
# numpy.set_printoptions(legacy= '1.13')
#
#
# new_list = list(map(float , input().split()))
# new_num = numpy.array(new_list)
# print(numpy.floor(new_num))
# print(numpy.ceil(new_num))
# print(numpy.rint(new_num))

""" Order dict library """
# from collections import OrderedDict
#
# my_order_dict  = {}
#
# n = int(input())
#
# for i in range(n) :
#     concent = list(input().split())
#     juice = concent[:-1]
#     juice = " ".join(juice)
#     try :
#         my_order_dict[juice] += int(concent[-1])
#     except :
#         my_order_dict[juice] = int(concent[-1])
#
# for juice in my_order_dict :
#     print(f"{juice} {my_order_dict[juice]}")

""" Exceptions"""
# n = int(input())
#
# for i in range(n):
#     try :
#         a , b = list(input().split())
#         print( int(a) // int(b))
#     except ZeroDivisionError  :
#         print("Error Code: integer division or modulo by zero")
#     except ValueError as e :
#         print(f"Error Code: {e}")

""" Company Logo"""
# #!/bin/python3
#
# mystring = str(input())
#
# my_dict = dict()
#
# for character in mystring:
#     my_dict[character] = my_dict.get(character , 0) + 1
#
#
# # Sort by value first, then by key length
# sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0][0])))
#
# sorted_list = list(sorted_dict)
# for i in range(3):
#     print(f"{sorted_list[i]} {sorted_dict[sorted_list[i]]}")
#
#

""" Piling up"""
# from collections import deque
#
# d = deque()
# n = int(input())
# for i in range(n):
#     result = True
#     m = int(input())
#     cubes = list(map(int, input().split()))
#     cubes = deque(cubes)
#     current_cube = max(cubes[0], cubes[-1])
#     print(len(cubes))
#
#     while True :
#         if len(cubes) == 0 :
#             break
#
#         if max(cubes[0] , cubes[-1]) > current_cube:
#             result = False
#             break
#         else :
#             current_cube = max(cubes[0] , cubes[-1])
#
#         if cubes[0] >= cubes[-1] :
#             cubes.popleft()
#         else :
#             cubes.pop()
#
#     if result :
#         print("Yes")
#     else :
#         print("No")

""" deque """
# from collections import deque
#
# n = int(input())
# d =deque()
#
# for i in range(n):
#     content = list(input().split())
#     command = content[0]
#
#     if command == "append":
#         d.append(int(content[1]))
#     elif command == "appendleft":
#         d.appendleft(int(content[1]))
#     elif command == "pop":
#         d.pop()
#     elif command == "popleft":
#         d.popleft()
#
# for number in d :
#     print(number , end= " ")

""" no idea !"""
# handle input
# n , m = map(int , input().split())
# happiness_numbers = list(map(int , input().split()))
# A_numbers = list(map(int, input().split()))
# B_numbers = list(map(int, input().split()))
#
# # solve problem
# A_count = {}
# for i in A_numbers:
#     A_count[i] = A_count.get(i , 1)
#
# B_count = {}
# for i in B_numbers :
#     B_count[i] = B_count.get(i , -1)
#
# happiness_index = 0
# for i in happiness_numbers :
#     happiness_index = happiness_index + A_count.get(i , 0) + B_count.get(i , 0)
#
# print(happiness_index)

""" word order"""
#
# word_count = {}
# n = int(input())
# list_words = []
# for i in range(n):
#     new_word = str(input())
#     list_words.append(new_word)
#     word_count[new_word] = word_count.get(new_word , 0) + 1
#
# print(len(word_count))
# for word in word_count :
#     print(word_count[word] , end= " ")

"""calendar """
# import calendar
#
# (month , day , year) = map(int , input().split())
#
# day_of_week = calendar.weekday(year, month, day)
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
# print(days[day_of_week].upper())

# """ No idea ! """
# m = map(int, input().split())
#
# happiness_numbers = set(map(int , input().split()))
# favorite_numbers = set(map(int, input().split()))
# hate_numbers = set(map(int, input().split()))
#
# happiness_index = len(happiness_numbers.intersection(favorite_numbers)) - len(happiness_numbers.intersection(hate_numbers))
#
# print(happiness_numbers)
# print("After that ")
# print(happiness_numbers)
#

""" set skills"""
# n = int(input())
# myset = set(map(int , input().split()))
#
# print(myset)
#
# quanity_command = int(input())
#
# for i in range(quanity_command):
#     command = list(input().split())
#     if len(command) > 0 :
#         new_set = set(input().split())
#
#     if command[0] ==  "intersection_update":
#         myset.intersection_update(new_set)
#     elif command[0] == "update":
#         myset.update(new_set)
#     elif command[0] == "symmetric_difference_update" :
#         myset.symmetric_difference_update(new_set)
#     elif command[0] == "difference_update" :
#         myset.difference_update(new_set)
#
#     print(myset)
#
# print(myset)

""" Find angle ABC """
# import math
#
# if __name__ == '__main__':
#     ab = int(input())
#     bc = int(input())
#     tan = ab / bc
#     print(f"{round(math.degrees(math.atan(tan)))}{chr(176)}")

"""swap case """
# def swap_case(s):
#     swapped_case = ""
#     for character in s :
#         if character.isupper():
#             swapped_case += character.lower()
#         else :
#             swapped_case += character.upper()
#     return swapped_case
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

""" Tuples """
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     integer_list = list(integer_list)
#     integer_tuples = tuple(integer_list)
#     # print(n)
#     # print("This is integer list ")
#     # print(integer_list)
#     print(hash(integer_tuples))

""" Threading """
# import threading
#
#
# def handle_thread_1(count):
#     for i in range(count):
#         print(f"Threading 1 : {i + 1}")
#         mess = input("Enter your messages (Thread 1 ) :  ")
#
#
# def handle_thread_2(count):
#     for i in range(count):
#         print(f"Threading 2 : {i + 1}")
#         mess = input("Enter your messages (Thread 2 ) :")
#
#
# count_1 = int(3)
# count_2 = int(5)
#
# thread_1 = threading.Thread(target=handle_thread_1, args=(count_1, ))
# thread_2 = threading.Thread(target=handle_thread_2, args=(count_2, ))
#
# thread_1.start()
# thread_2.start()
# print("Main function are running ! ")
#
# thread_2.join()
# thread_1.join()
#
#
# print("All threadings are done ! ")

""" 5. List """
# if __name__ == '__main__':
#     N = int(input())
#     my_list = []
#     for i in range(N):
#         data = input().split()
#
#         if data[0] =="insert":
#             my_list.insert(int(data[1]) , int(data[2]))
#         elif data[0] == "print":
#             print(my_list)
#         elif data[0] == "remove":
#             my_list.remove(int(data[1]))
#         elif data[0] == "sort":
#             my_list.sort()
#         elif data[0] == "append":
#             my_list.append(int(data[1]))
#         elif data[0] == "pop":
#             my_list.pop()
#         elif data[0] == "reverse":
#             my_list.reverse()
#


""" 4. Text Alignment"""
# outline = str('H')
# thickness = 5 #int(input("Enter thickness in here :"))
# outline = outline * thickness
#
# # draw
# # print(outline.center(thickness*2 -1 , ' '))
# char_angle = 'H'
# space = "HHHHH               HHHHH"
# for i in range(1 , 2 * thickness , 2):
#     print(char_angle.center(2 * thickness - 1, ' '))
#     char_angle = char_angle + "HH"
#
# width = len(space) + 4
# for i in range(6):
#     print(space.center(width , ' '))

""" 3. String Validators """
# if __name__ == '__main__':
#     s = "WWWWWWWWWWWWW"
#     check_alphanumeric = False
#     check_alphabetical = False
#     check_digit = False
#     check_lowercase = False
#     check_uppercase = False
#
#     for character in s :
#         if character.isalnum() :
#             check_alphanumeric = True
#         if character.isalpha() :
#             check_alphabetical = True
#         if character.isdigit() :
#             check_digit = True
#         if character.islower():
#             check_lowercase = True
#         if character.isupper():
#             check_uppercase = True
#
#     print(check_alphanumeric)
#     print(check_alphabetical)
#     print(check_digit)
#     print(check_lowercase)
#     print(check_uppercase)
#     # check has any alphanumeric
#     # check has any alphabetical
#     # check has any digits
#     # check has any lowercase
#     # check has ant uppercase



""" Finding the percentage """

# def average(numbers):
#     sum = 0
#     for number in numbers :
#         sum += number
#
#     sum = sum / 3
#     formatted = f"{sum:.2f}"
#     print(formatted)
#
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     # display output
#     average(student_marks[query_name])
