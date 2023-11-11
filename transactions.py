# Script that runs the transactions


from user_auth import Login

class Transactions():
  # import information from log in to see if you are logged on (mainly status)
  def transaction(from_account, to_account, amount, user_name, password): # from and to_accounts are dataframe of each user and rows are transactions
    # if this is the first transaction ever, or if previous amount is zero, give error message 'Add more funds'
    from_account.loc[len(from_account.index)] = [] # transaction date, previous amount -  amount
    x = from_account.loc[len(from_account.index)-1]
    # if transfering out of your account then from_account=from_account
    # if you're receiving a transfer then from_account=to_account
    new_balance = Transactions.checkBalance(from_account=from_account, user_name=user_name, password=password)
    return x # return modified row

  def addBalance(your_account, amount, user_name, password):
    # if this is first time adding balance, just add the amount as the first  transaction

    if len(your_account) == 0:
        # you haven't had any transactions yet so add to the account
        your_account.loc[len(your_account)] = [10111, 'tesh pierre', user_name, password, amount, 'deposit', amount] # include today date&time
        print(your_account) # transaction date, previous amount +  amount or use .append()
        # ['account_id', 'name', 'user_name', 'password', 'balance', 'transaction_type', 'transaction_amount']
    else:
      prev_amount = float(your_account.loc[(len(your_account.index))-1, 'balance'])
      new_balance = prev_amount + amount
      your_account.loc[len(your_account)] = [10111, 'tesh pierre', user_name, password, new_balance, 'deposit', amount]
      print(your_account)
    return

  def checkBalance(your_account, user_name, password):
    balance = round(your_account.loc[len(your_account.index)-1, 'balance'], 2)
    return print('Your current account balance is: $', balance)

  def transRequest(from_account, to_account, user_name, password, approve):
    if approve == True:
      Transactions.transaction(from_account=to_account, to_account=from_account)
      new_balance = Transactions.checkBalance(from_account=from_account, user_name=user_name, password=password)
      x = new_balance
    else:
      x = print('Request denied')

    return