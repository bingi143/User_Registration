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
    pattern=r'^[A-Z][a-z]{3,}$'
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
    pattern=r'^[A-Z][a-z]{3,}$'
    if re.fullmatch(pattern,last_name):
        return True

    else:
        return False

def emial_verification(email):
    '''
          Description: 
                This function is check email valid or not
          Parameters: 
                last_name(str): string
          Return : 
                None
    '''
    pattern=  r'^abc+\.*[a-zA-Z0-9._%+-]*@bl+\.co+$'
    if re.match(pattern,email):
        return True
    else:
        return False


def main():
    first_name=input("Enter first name:")
    last_name=input("Enter last name:")
    email=input("Enter email:")
    if checking_first_name(first_name):
         logger_init("UC_1").info("User first name is valid")
    else:
        logger_init("UC_1").info("User first name is not valid")

    if checking_last_name(last_name):
        logger_init("UC_2").info("user last name is valid")
    else:
        logger_init("UC_2").info("user last name is not valid")

    if emial_verification(email):
        logger_init("UC_3").info("user email is valid")
    else:
        logger_init("UC_3").info("user email is not valid")


if __name__=="__main__":
    main()