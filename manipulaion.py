# In a paragraph replace a “is” with “was” . then count no of “a” in a paragraph.
# para = input("Enter a para:")
# modified_para=para.replace("is", "was")
# count_a=modified_para.count('a')
# print("modified para:", modified_para)
# print("count of 'a':", count_a)

# get a input from user also check  its valid password.
# password = input("Enter your password: ")
# digit = any(char.isdigit() for char in password)
# letter = any(char.isalpha() for char in password)
# if digit and letter("password:"):
#     print("Valid Password:",digit)
# else:
#     print("Invalid Password:",letter)



# def login(username_input, password_input, username, password):
#     if username_input == username and password_input == password:
#         return "Login successful!"
#     else:
#         return "Invalid input."
# username = "keerthana"
# password = "123456"
# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")
# print(login(username_input, password_input, username, password))


# digit = any(char.isdigit() for char in password)
# letter = any(char.isalpha() for char in password)



email=input("Enter your email")
if '@' in email and '.' in email:
    print("valid mail id")
else:
    print("invalid mail id")