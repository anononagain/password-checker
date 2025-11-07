# ISTG THIS IS LIKE MY FIRST CYBERSEC PROJECT, EXCITED

# ----------------------------
# Password Strength Checker
# ----------------------------
# This small program will check if a password is strong or not hehe

# Importing re (Used to search patterns in text)
import re

def check_password_strength (password):
    '''
    
    Check the strength of a given password.
    Rules:
       - At least 8 Characters long
       - Contains an Uppercase letter
       - Contains a lowercase letter
       - Contains digit (numbers)
       - Contains a special character (ex: @, #, !)
    '''    
    if len(password) < 8: #Checks the length of the password
        return "Weak: password must be atleast 8 characters."
    
    if not any(char.isdigit() for char in password):
        return "Weak: password must contain a digit."
    
    if not any(char.isupper() for char in password):
        return "Weak: password must contain an upper character"
    
    if not any(char.islower() for char in password):
        return "Weak: password must contain a lower character"
    
    if not re.search(r'[!@#$%^&*(){<>.,?}_=+-`~/|]', password):
        return "Weak: password must contain a special character"
    return "Strong: Your password is secured!"

def password_checker():
    print("Welcome to the password strenth checker")

    while True:
        password = input("Enter your password (or type 'exit to quit): ")
        
        if password.lower() == 'exit':
            print("Thank you for using this tool!")
            break
        
        result = check_password_strength(password)
        print(result)

# Run the password checker tool.
if __name__ == "__main__":
    password_checker()