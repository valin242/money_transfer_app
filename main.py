#
# Money Transfer Application
#
# @author: 2pitesh
#

import pandas as pd
import numpy as np
from user_auth import Login
from transactions import Transactions

# Check if user is login. If not, ask user to log inaccounts = pd.DataFrame(columns=['account_id', 'name', 'user_name'])

# Example dfs for accounts and transactions for Testing
accounts_secure = pd.DataFrame(columns=['account_id', 'name', 'user_name', 'password'])
my_account = pd.DataFrame(columns=['account_id', 'name', 'user_name', 'password', 'balance', 'transaction_type', 'transaction_amount'])
my_balance = pd.DataFrame(columns=['account_id', ])

# details = np.array([11243423, 'tesh pierre', username, pwd, 50, 'deposit', 50.00])
# my_account.loc[len(my_account)] = details # manually adds a transaction

def auth():
    # authenticate user before going to main
    
    #Login.login()
    username = 'valin242'
    pwd = 'valin424'


    # if authenticated, then run main
    main()

    return


def main():
    print("Welcome to the money app")
    query = input("Do you want to 'send'/'request', or 'add' balance? ")
    while query != '' or query !='no':
        if query == 'add':
            amount = input('How much do you want to add to your account? ')
            Transactions.addBalance(my_account, float(amount), 'valin242', 'valin424')
            q = input('Do you want to make another?')
            if q == 'yes':
                query == 'add'
            else:
                query = 'no'
                continue

        elif query == 'send':
            d = 2
        elif query == 'request':
            d = 3
        else: 
            query = input("Re-enter the type of transaction (send, request, add): ")
    else:
        print("Thank you for checking out the app")
        


if __name__ == "__main__":
    auth()

