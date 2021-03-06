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
    
     # ...Test Case --3

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("Test","user","0700000000","test@user.com") # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)
        
        
    #...Test Case--4
    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account("Test","user","0700000000","test@user.com") # new account
        test_account.save_account()

        self.new_account.delete_account()# Deleting a account object
        self.assertEqual(len(Account.account_list),1)
    
    
     #...Test Case--5
    def test_find_account_by_number(self):
        '''
        test to check if we can find a account by phone number and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0700000000","test@user.com") # new account
        test_account.save_account()

        found_account = Account.find_by_number("0700000000")

        self.assertEqual(found_account.email,test_account.email)   
        
    #...Test Case---6     
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0700000000","test@user.com") # new account
        test_account.save_account()

        account_exists = Account.account_exist("0700000000")

        self.assertTrue(account_exists)   
        
     #...Test Case---7
    def test_display_all_accounts(self):
        '''
        method that returns a list of all account saved
        '''

        self.assertEqual(Account.display_accounts(),Account.account_list)
        
if __name__ ==  '__main__':
    unittest.main()
        