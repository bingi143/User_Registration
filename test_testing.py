'''

@Author: Venkatesh
@Date: 2024-09-04 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-09-04 18:00:30
@Title : Program Aim to py-testing testing on user registration


'''


import pytest
from user_registration import checking_first_name


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


def main():
    test_checking_first_name()


if __name__=="__main__":
    pytest.main()
