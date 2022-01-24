#!/usr/bin/env python3.8.10

from account import Account
from credential import Credential

#Creating a Account Function
def create_account(fname,lname,phone,email,password):
    
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email,password)
    return new_account

#   Save account Function
def save_account(account):
    
    '''
    Function to save account
    '''
    account.save_account()

 #Delete account Function
def delete_account(account):
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

# Function to Check if an account exists
def check_existing_account(number):
    '''
    Function that check if a account exists with use of number and return a Boolean
    '''
    return Account.account_exist(number)

    #  Displaying all accounts   
def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()





def login_user(password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credential.verify_user(password)
    return check_user

def create_new_credential(password):
    """
    Function that creates new credential for a given user account
    """
    new_credential = Credential(password)
    return new_credential
def save_credential(credential):
    """
    Function to save Credential to the credential list
    """
    credential. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credential.display_credential()

def delete_credential(credential):
    """
    Function to delete a Credential from credential list

    """
    credential.delete_credential()

def find_credential(account):
    """
    Function that finds a Credential by an account name and returns the Credential that belong to that account
    """
    return Credential.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credential exists with that account name and return true or false

    """
    return Credential.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credential.generatePassword()
    return auto_password

# Main call
# Main function to call 
def main():
    
    
    
    print("                  _____                   _                   _                   ")
    print("                 |  __ \                 | |                 | |                  ")
    print("                 | |__) |__ _  ___  ___  | |      ___    ___ | | __ ___  _ __     ")
    print("                 |  ___// _` |/ __|/ __| | |     / _ \  / __|| |/ // _ \| '__|    ")
    print("                 | |   | (_| |\__ \\__ \ | |____| (_) || (__ |   <|  __/| |       ")
    print("                 |_|    \__,_||___/|___/ |______|\___/  \___||_|\_\\___||_|       ")
    print("                                                                                  ")
    print("                                                                                  ")
    print("                       ..................................................         ")
    print("                    .........................................................     ")
    
    
    print("                     Hello, Welcome to Account creation app. What is your name?    ")
    
    user_name = input()
    print(f"Welcome {user_name},")
            
    while True:
        
        print("Use these short codes : \n 1. Create a new account\n 2. Display accounts\n 3. Find a account\n 4. Exit the account list ")

        short_code = input().lower()

        if short_code == '1':
            print("New Account")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()
            
            
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password = input().lower().strip()
                        
            if password == 'tp':
                password = input("Enter Password\n")
                
            elif password == 'gp':
                password = generate_Password()
                
            else:
                            print("Invalid password please try again")
                
            save_account(create_account(f_name,l_name,p_number,e_address,password)) # create and save new account.
            print ('\n')
            print(f"New Account {f_name} {l_name} created, Your password is: {password}")
            print ('\n')
            
            

        elif short_code == '2':
            
            if display_accounts():
                    print("H..................................")
                    print("\nHere is a list of all your accounts")
                    print("...................................")
                    print('\n')

                    for account in display_accounts():
                        print(f"{account.first_name} {account.last_name} .....{account.phone_number}")
                        print('\n')
                        
                    else:
                        print('\n')
                        print(".............................................")
                        print("\nYou dont seem to have any accounts saved yet")
                        print(".............................................")
                        
                        print('\n')
            elif short_code == '3':
                  print("\nEnter the number you want to search for")
                  search_number = input()
                  
                  if check_existing_account(search_number):
                      search_account = find_account(search_number)
                      print(f"{search_account.first_name} {search_account.last_name}")
                      print('-' * 20)
                      print(f"Phone number.......{search_account.phone_number}")
                      print(f"Email address.......{search_account.email}")
            else:
                
                print("\nThat account does not exist")
                print("...........................")
        elif short_code == '5':
            print('enter the account you want to delete')
            if delete_account():
                for account in delete_account():
                        print(f"{account.first_name} {account.last_name} .....{account.phone_number} deleted successfully")
                        print('\n')
                        
                else:
                        print('\n')
                        print(".............................................")
                        print("\nYou dont seem to have any accounts saved yet")
                        print(".............................................")
                        
                        print('\n')
        
            
              
        elif short_code == "4":
            
            print("\nBye .......")
            break
        else:
            print("\nI really didn't get that. Please use the short codes")
            print("....................................................")
            
        
            
        
# if __name__ == '__main__':
    
#     
main()