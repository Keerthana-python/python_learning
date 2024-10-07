# array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evennumber=[]
# oddnumber=[]
# for i in array:
#     if i%2==0:
#         evennumber.append(i)
#     else:
#         oddnumber.append(i)
# print("evennumber:",evennumber)
# print("oddnumber:", oddnumber)

array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3]
new=(2, 3)
duplicates=[]
for i in array:
    if i in new and i not in duplicates:
        duplicates.append(i)
print("duplicates:", duplicates)


# array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# sum = sum(array)
# print("Sum of the list:", sum)

# array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# product = 1
# for num in array:
#     if num != 0:
#         product *= num
# print("Product of the list ignor zero:", product)

# array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3]
# duplicates = list(2, 3)
# for num in array:
#     if array.count(num) > 1:
#         print("Duplicate elements:",duplicates)

# array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reversed_list = array[::-1]
# print("Reversed list:", reversed_list)

# array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# largest = 10
# smallest = 1
# for num in array:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("Largest number:", largest)
# print("Smallest number:", smallest)

