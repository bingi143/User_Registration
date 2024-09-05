'''

@Author: Venkatesh
@Date: 2024-09-04 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-09-04 18:00:30
@Title : Program Aim to unit testing on user registration


''' 

import unittest
from user_registration import checking_first_name,checking_last_name,email_verification
 
class TestingUserRegistarion(unittest.TestCase):
    
    def test_first_name(self):
        self.assertTrue(checking_first_name("Monkey"))
        self.assertFalse(checking_first_name("23Vwe"))
        self.assertTrue(checking_first_name("Venkatesh"))
        self.assertFalse(checking_first_name("juewf"))

    def test_last_name(self):
        self.assertTrue(checking_last_name("Bingi"))
        self.assertFalse(checking_last_name("ponkey"))
        self.assertTrue(checking_last_name("Sweet"))
        self.assertFalse(checking_last_name("venkat"))

    def test_email(self):
        self.assertTrue(email_verification("venky@bl.co.in"))
        self.assertTrue(email_verification("abc.xyz@bl.co"))
        self.assertTrue(email_verification("123@bl.co"))
        self.assertFalse(email_verification("venkybl.co"))
        self.assertFalse(email_verification("@venkatbl.co"))
        self.assertFalse(email_verification("Venky@blco."))

 
def main():
    t1=TestingUserRegistarion()
    t1.test_first_name()
    t1.test_last_name()


if __name__=="__main__":
     unittest.main()