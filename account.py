class Account:
  
  """
  Class that generates new instances of account details.
  """
  account_list = [] # Empty contact list

   # saving account method
  def save_account(self):
    
    '''
    save_account method saves account objects into account_list
    '''

    Account.account_list.append(self)


  # deleting account method
  def delete_account(self):
    '''
    delete_account method deletes a saved account from the account_list
    '''
    Account.account_list.remove(self)
    
  @classmethod
  def find_by_number(cls,number):
      '''
      Method that takes in a number and returns a account that matches that number.

      Args:
          number: Phone number to search for
      Returns :
          Account of person that matches the number.
      '''

      for account in cls.account_list:
          if account.phone_number == number:
              return account
              
    
    
    
      

  def __init__(self,first_name,last_name,number,email):
    
    
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = number
    self.email = email