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

def main():
    first_name=input("Enter first name:")
    if checking_first_name(first_name):
         logger_init("UC_1").info("User first name is valid")
    else:
        logger_init("UC_1").info("User first name is not valid")


if __name__=="__main__":
    main()