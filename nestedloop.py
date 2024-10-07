# pattern 3
# for i in range(1,6):
#     for j in range(1,6):
#         print(j, end="")
#     print()

# pattern 5
# for i in range(5):
#     for j in range(5, 0, -1):
#         print(j, end="")
#     print()

# pattern 1
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()


# row=int(input("enter a row value"))
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# row=5
# for i in range(1, row+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# rows=5
# for i in range(65, 65+rows):
#     for j in range(rows):
#         print(chr(i), end="")
#     print()

rows = 5
for i in range(rows):
    for j in range(rows):
        if(i+j)%2==0:
            print(1, end="")
        else:
            print(0, end="")
    print()

# rows=5
# for i in range(rows):
#     for j in range(69, 64, -1):
#         print(chr(j), end="")
#     print() 

        



