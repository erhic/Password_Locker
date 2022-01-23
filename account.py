class Account:
    """
    Class that generates new instances of account details.
    """

    account_list = [] # Empty contact list

    def save_account(self):

            '''
            save_account method saves account objects into account_list
            '''

            Account.account_list.append(self)




    def __init__(self,first_name,last_name,number,email):

  

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email