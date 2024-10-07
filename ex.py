# prin numbers from list that are > 10
list = [5, 7, 18, 20, 2, 36]
for x in list:
    if x>10:
        print(x)

# find the largest number in a list
num=[12, 30, 3, 15, 10]
largest=max(num)
print(largest)

# count the number of vowels in a string
list="welcome to our home"
vowel="aeiou"
count=1
for char in list:
    if char in vowel:
        count+=1
print(count)

# print product pf numbers from 1 to 5
product=1
for i in range(1,6):
    product*=i
print(product)

