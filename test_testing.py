'''

@Author: Venkatesh
@Date: 2024-09-04 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-09-04 18:00:30
@Title : Program Aim to unit testing on user registration


''' 

import pytest
from user_registration import checking_first_name,checking_last_name,email_verification,check_mobile_formet,checking_password


def test_checking_first_name():
    '''
        Description: 
                This function is testing the first name is valid
        Parameters: 
                None
        Return : 
                None
    '''
    assert checking_first_name("Venaktesh")==True
    assert checking_first_name("Tejaswini")==True
    assert checking_first_name("Vijay")==True
    assert checking_first_name("sanju")==False
    assert checking_first_name("venkatesh")==False
    assert checking_first_name("Te")==False


def test_checking_last_name():
    '''
        Description: 
                This function is testing the last name is valid
        Parameters: 
                None
        Return : 
                None
    '''
    assert checking_last_name("Bingi")==True
    assert checking_last_name("Daggu")==True
    assert checking_last_name("Boda")==True
    assert checking_last_name("kethineni")==False
    assert checking_last_name("basam")==False
    assert checking_last_name("bridge")==False

def test_checking_email():
    '''
        Description: 
                This function is testing the mail
        Parameters: 
                None
        Return : 
                None
    '''
    assert email_verification("Venaky@bl.co")==True
    assert email_verification("abc.xyz@bl.co")==True
    assert email_verification("123@bl.co")==True
    assert email_verification("venkybl.co")==False
    assert email_verification("bingi@.co")==False
    assert email_verification("venkat@blco")==False


def test_checking_mobile_number():
    '''
        Description: 
                This function is testing the mobile number fomate
        Parameters: 
                None
        Return : 
                None
    '''
    assert check_mobile_formet("91 9078563412")==True
    assert check_mobile_formet("81 9876540321")==True
    assert check_mobile_formet("00 8907654321")==True
    assert check_mobile_formet("9 9099909090")==False
    assert check_mobile_formet("91 89677")==False
    assert check_mobile_formet("9078563412")==False


def test_checking_password_matching():
    '''
        Description: 
                This function is testing the password having 8 charecters and more and one capilatal latter and one numeric number
                exactly one special charecter
        Parameters: 
                None
        Return : 
                None
    '''
    assert checking_password("we345Ws#df24")==True
    assert checking_password("12Weq$w12er")==True
    assert checking_password("abDde@asas1")==True
    assert checking_password("BqwqwWW12")==False
    assert checking_password("<.121@32")==False
    assert checking_password("!@#$%^&**")==False


def main():
    test_checking_first_name()
    test_checking_last_name()
    test_checking_email()
    test_checking_mobile_number()
    test_checking_password_matching()


if __name__=="__main__":
    pytest.main()