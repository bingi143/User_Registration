'''

@Author: Venkatesh
@Date: 2024-09-04 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-09-04 18:00:30
@Title : Program Aim to unit testing on user registration


''' 

import unittest
from user_registration import checking_first_name,checking_last_name,email_verification,check_mobile_formet,checking_password
 
class TestingUserRegistarion(unittest.TestCase):
    
    def test_first_name(self):
        '''
          Description: 
                This function is testing the first name with starting capital latter
          Parameters: 
                None
          Return : 
        '''
        self.assertTrue(checking_first_name("Monkey"))
        self.assertFalse(checking_first_name("23Vwe"))
        self.assertTrue(checking_first_name("Venkatesh"))
        self.assertFalse(checking_first_name("juewf"))

    def test_last_name(self):
        '''
          Description: 
                This function is testing the last name with starting capital latter
          Parameters: 
                None
          Return : 
                None
        '''
        self.assertTrue(checking_last_name("Bingi"))
        self.assertFalse(checking_last_name("ponkey"))
        self.assertTrue(checking_last_name("Sweet"))
        self.assertFalse(checking_last_name("venkat"))

    def test_email(self):
        '''
          Description: 
                This function is testing the email formate
          Parameters: 
                None
          Return : 
                None
        '''
        self.assertTrue(email_verification("venky@bl.co.in"))
        self.assertTrue(email_verification("abc.xyz@bl.co"))
        self.assertTrue(email_verification("123@bl.co"))
        self.assertFalse(email_verification("venkybl.co"))
        self.assertFalse(email_verification("@venkatbl.co"))
        self.assertFalse(email_verification("Venky@blco."))

        self.assertTrue(email_verification("abc@yahoo.com"))
        self.assertTrue(email_verification("abc-100@yahoo.com"))
        self.assertTrue(email_verification("abc.100@yahoo.com"))
        self.assertTrue(email_verification("abc111@abc.com"))
        self.assertTrue(email_verification("abc111@abc.net"))
        self.assertTrue(email_verification("abc.100@abc.com.au"))
        self.assertTrue(email_verification("abc@1.com"))
        self.assertTrue(email_verification("abc@gmail.com.com"))
        self.assertTrue(email_verification("abc+100@gmail.com"))
        self.assertFalse(email_verification("abc"))
        self.assertFalse(email_verification("abc@.com.my"))
        self.assertFalse(email_verification("abc123@gmail.a"))
        self.assertFalse(email_verification("abc123@.com"))
        self.assertFalse(email_verification("abc123@.com.com"))
        self.assertFalse(email_verification(".abc@abc.com"))
        self.assertFalse(email_verification("abc()*@gmail.com"))
        self.assertFalse(email_verification("abc@%*.com"))
        self.assertFalse(email_verification("abc..2002@gmail.com"))
        self.assertFalse(email_verification("abc.@gmail.com"))
        self.assertFalse(email_verification("abc@abc@gmail.com"))
        self.assertFalse(email_verification("abc@gmail.com.1a"))
        self.assertFalse(email_verification("abc@gmail.com.aa.au"))
    

    def test_mobile_number(self):
        '''
          Description: 
                This function is testing the phone number
          Parameters: 
                None
          Return : 
                None
        '''
        self.assertTrue(check_mobile_formet("91 6305114038"))
        self.assertTrue(check_mobile_formet("88 5453534212"))
        self.assertTrue(check_mobile_formet("71 9087654312"))
        self.assertFalse(check_mobile_formet("916305114038"))
        self.assertFalse(check_mobile_formet("91 63051140"))
        self.assertFalse(check_mobile_formet("8 6305114038"))
    
    def test_password(self):
        '''
          Description: 
                This function is testing the password pattern
          Parameters: 
                None
          Return : 
                None
        '''
        self.assertTrue(checking_password("we345W^sdf24"))
        self.assertTrue(checking_password("12234F#35342"))
        self.assertTrue(checking_password("QWERT@5YUIOP"))
        self.assertFalse(checking_password("!@#$%^&**"))
        self.assertFalse(checking_password("12Wsd3asd"))
        self.assertFalse(checking_password("po@3iuy"))
        self.assertFalse(checking_password("<>wewe12"))


def main():
    t1=TestingUserRegistarion()
    t1.test_first_name()
    t1.test_last_name()


if __name__=="__main__":
     unittest.main()