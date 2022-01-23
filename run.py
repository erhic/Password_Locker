#!/usr/bin/env python3.8.10

from account import Account
from credential import Credential

#Creating a Account Function
def create_contact(fname,lname,phone,email):
    
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email)
    return new_account

#   Save account Function
def save_account(account):
    
    '''
    Function to save account
    '''
    account.save_account()

 #Delete account Function
def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()
    
 #Finding an account Function
def find_account(number):
    '''
    Function that finds a account by number and returns the account
    '''
    return Account.find_by_number(number)

    