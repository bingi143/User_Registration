'''

@Author: Venkatesh
@Date: 2024-09-04 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-09-04 18:00:30
@Title : Program Aim to create user registration


''' 
from my_logging import logger_init
import re

def checking_first_name(first_name):
    '''
          Description: 
                This function is check the first name
          Parameters: 
                first_name(str): string
          Return : 
                None
    '''
    pattern=r'^[A-Z][a-z]{2,}$'
    if re.match(pattern,first_name):
        return True

    else:
        return False

def checking_last_name(last_name):
    '''
          Description: 
                This function is check the last name
          Parameters: 
                last_name(str): string
          Return : 
                None
    '''
    pattern=r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern,last_name):

        return True

    else:
        return False

def email_verification(email):
    '''
          Description: 
                This function is check email valid or not
          Parameters: 
                last_name(str): string
          Return : 
                None
    '''
    
    pattern=r"^[a-z0-9A-Z]+(?:[._%+-][a-zA-Z0-9]+)*@[a-z0-9-A-Z]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$"
    if re.match(pattern,email):
        return True
    else:
        return False
    
def attempt_input(prompt, validation_func, logger_tag, error_message):
    '''
          Description: 
                This function prompts the user for input and validates it with retries
          Parameters: 
                prompt(str): the input prompt message
                validation_func(function): function to validate input
                logger_tag(str): log tag for logging valid/invalid attempts
                error_message(str): error message to display after failed validation
          Return : 
                Valid input or None if attempts exhausted
    '''
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        user_input = input(prompt)
        if validation_func(user_input):
            logger_init(logger_tag).info(f"User {prompt.strip(':')} is valid")
            return user_input
        else:
            logger_init(logger_tag).info(f"User {prompt.strip(':')} is not valid")
            attempts += 1
            print(f"{error_message} You have {max_attempts - attempts} attempt(s) left.")
    
    print("Your time is over.")
    return None

def check_mobile_formet(mobile_number):
    '''
          Description: 
                This function is checking phone number valid formate or not
          Parameters: 
                mobile_number(int): number
          Return : 
                None
    '''
    pattern=r'^[0-9]{2}\s[0-9]{10}$'
    if re.match(pattern,mobile_number):
        return True
    else:
        return False
    
def checking_password(password):
    '''
          Description: 
                This function is checking password al least one upper case
          Parameters: 
                mobile_number(int): number
          Return : 
                None
    '''
    pattern = r"^(?=.*[A-Z])(?=.*[0-9])(?=[^@#$%^&+=]*[@#$%^&+=][^@#$%^&+=]*$)[A-Za-z0-9@#$%^&+=]{8,}$"
    if re.match(pattern,password):
        return True
    else:
        return False

def main():
    first_name = attempt_input("Enter first name: ", checking_first_name, "UC_1", "Invalid first name.")
    if first_name is None:
        return  

    last_name = attempt_input("Enter last name: ", checking_last_name, "UC_2", "Invalid last name.")
    if last_name is None:
        return  

    email = attempt_input("Enter email: ", email_verification, "UC_3", "Invalid email.")
    if email is None:
        return 
    mobile_number = attempt_input("Enter phone number: ", check_mobile_formet, "UC_4", "Invalid mobile formate enter country code space and number.")
    if mobile_number is None:
        return 
    password = attempt_input("Enter password: ", checking_password, "UC_5", "Invalid password enter minimum 8 charecters")
    if password is None:
        return 


if __name__=="__main__":
    main()