#!/usr/bin/env python3.8.10

from account import Account
from credential import Credential

#Creating a Account
def create_contact(fname,lname,phone,email):
    
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email)
    return new_account
