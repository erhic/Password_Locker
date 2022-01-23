import unittest # Importing the unittest module
from account import Account # Importing the account class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases;subclass
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Abdi","Mustafa","0723232457","abdi@yahoo.com") # create account object
        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []
   
   
       #Test Case -1      
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.first_name,"Abdi")
        self.assertEqual(self.new_account.last_name,"Mustafa")
        self.assertEqual(self.new_account.phone_number,"0723232457")
        self.assertEqual(self.new_account.email,"abdi@yahoo.com")

    # ...  Test Case--2
    
    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list /appended
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)
    
     # ..  Test--3

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0700000000","test@user.com") # new contact
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)
            