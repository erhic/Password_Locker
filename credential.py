
import random
import string

class Credential:

    credential_list = []

    def __init__(self,password):
        '''
        function helps us define properties of our objects
        '''
        self.password = password 

    def save_credential(self):
        '''
        function to save user credentials
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        function to delete user credentials
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def display_credential(cls):
        '''
        function to display all user credentials
        '''
        return cls.credential_list

    def generatePassword(length=5):
        """Generate a random password string of letters and digits and special characters"""
       
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
       
        return result_str 
    @classmethod
    def credential_exist (cls,account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credential_list:
            if credential.account==account:
                return True
            return False
        
    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential