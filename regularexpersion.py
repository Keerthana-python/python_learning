import re

# text="hi welcome to our sweet home"
# result=re.findall("\S",text)
# print(result)

# txt = "My name is Jai Ksihore. I am, currently learning python to upgrade my skill set at Ocean Academy.My details to to login email id: jai123@gmail.com ,contact number : 7896543211 , contact address: vengata nagar ,pondicherry - 606356"

# email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# phone = r'\b\d{10}\b'
# pincode = r'\b\d{6}\b'
# email = re.findall(email, txt)
# phone = re.findall(phone, txt)
# pincode = re.findall(pincode, txt)
# print("Email ID:", email[0] if email else "Not found")
# print("Mobile Number:", phone[0] if phone else "Not found")
# print("Pin Code:", pincode[0] if pincode else "Not found")

def validate_name(name):
    if re.fullmatch(r'[A-Za-z\s]+', name):
        return True
    else:
        return False

# Function to validate email
def validate_email(email):
    if re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return True
    else:
        return False

# Function to validate phone number (10 digits)
def validate_phone(phone):
    if re.fullmatch(r'\d{10}', phone):
        return True
    else:
        return False

# Function to validate course code (e.g., CS101, ENG202)
def validate_course_code(course_code):
    if re.fullmatch(r'[A-Z]{2,4}\d{3}', course_code):
        return True
    else:
        return False

# Function to collect and validate registration form input
def course_registration():
    print("Welcome to the Course Registration Form")
    
    # Get and validate name
    while True:
        name = input("Enter your full name: ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please enter letters and spaces only.")
    
    # Get and validate email
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        else:
            print("Invalid email format. Example: name@example.com")

    # Get and validate phone number
    while True:
        phone = input("Enter your 10-digit phone number: ")
        if validate_phone(phone):
            break
        else:
            print("Invalid phone number. It should be exactly 10 digits.")

    # Get and validate course code
    while True:
        course_code = input("Enter the course code (e.g., CS101): ")
        if validate_course_code(course_code):
            break
        else:
            print("Invalid course code. Format: 2-4 uppercase letters followed by 3 digits (e.g., CS101).")
    
    print("\nRegistration Successful!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Course Code: {course_code}")
course_registration()



  





