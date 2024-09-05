'''

@Author: Venkatesh
@Date: 2024-09-04 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-09-04 18:00:30
@Title : Program Aim to unit testing on user registration


''' 

import unittest
from user_registration import checking_first_name
 
class TestingUserRegistarion(unittest.TestCase):
    
    def test_first_name(self):
        '''
          Description: 
                This function is testing the first name have start with capital
          Parameters: 
                None
          Return : 
                None
        '''
        self.assertTrue(checking_first_name("arn"))
        self.assertFalse(checking_first_name("23Vwe"))
        self.assertTrue(checking_first_name("VenKy"))
        self.assertFalse(checking_first_name("Juewf"))


def main():
    t1=TestingUserRegistarion()
    t1.test_first_name()


if __name__=="__main__":
     unittest.main()