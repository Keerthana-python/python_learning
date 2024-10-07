# def number(num):
#    if num < 1:
#       return
#    print(num)
#    number(num - 1)
# number(10)

# def number(num):
#    if num < 1:
#       return
#    number(num - 1)
#    print(num)
# number(10)

# def fibonacci(num):
#    if num <= 1:
#       return num
#    return fibonacci(num - 1) + fibonacci(num - 2)
# for i in range(10):
#    print(fibonacci(i), end=" ")

# def sum(list):
#    if len(list) == 1:
#       return 1
#    return list[1] + sum(list[1:])
# list = [1, 2, 3, 4, 5]
# print(sum(list))

# map, reduce, filter
# x = [1, 2, 3, 4, 5]
# square = list(map(lambda x: x**2, x))
# print("square:",square)

# x = ["welcome to our home"]
# uppercase = set(map(str.upper,x))
# print("uppercase:",uppercase)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# added = list(map(lambda x: x + 10, x))
# print("added:",added)

# x = [5, 6, 8, 2, 9, 4, 3, 1]
# double = list(map(lambda x: x * 2, x))
# print("double:",double)

# x = ["python", "java", "c++", "javascript"]
# capitalized = tuple(map(str.capitalize, x))
# print(capitalized)

# x = [2, 3, 7, 5, 8, 16, 18, 9, 10]
# even = list(filter(lambda x: x % 2 == 0, x))
# print("even:",even)

# x = ["keerthu", "sri", "bala", "barath", "ten"]
# filter = tuple(filter(lambda x: len(x) >= 4, x))
# print("filter:", filter)

# x = [7, 3, 16, 5, 15, 2, 8, 13, 14]
# filter = set(filter(lambda x: x <= 10, x))
# print("filter",filter)

# x = ["keerthu", "sri", "bala", "barath", "ten"]
# filter = list(filter(lambda x: 'a' not in x, x))
# print("filter:",filter)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
# filter = tuple(filter(lambda x: x % 3 == 0, x))
# print("filter:",filter)








