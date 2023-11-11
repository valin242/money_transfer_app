'''
Get some notes from here: https://medium.com/@mycodingmantras/designing-a-login-register-and-user-authentication-script-in-python-326a11821504
https://thecleverprogrammer.com/2021/05/02/password-authentication-using-python/

One class for user_auth to include login, logout, register
Another class for transactions
'''
class Login(object): # does authentication need to be a separate class?
  
#   def __init__(self, user_name, password):
#     self.user_name = str(user_name)
#     self.password = str(password)
#     self.status = False
  def login():
    user_name = input("Enter username:")
    pwd = input("Enter password:")
    # change so that you only require username and password for login
    # if the username and password matches what is in the database, then status True
    if user_name == 'valin242':
      if pwd == 'valin424':
        status = print('You are logged in')
      else:
        status = print('Incorrect Password')
    else:
      status = print('Incorrect user name')

    return status

  def logout():
    status = False
    return print("You are logged out")

  def signUp(): # sign up creates a new user name and password and logs you in
    # ask for user name, password, name (can add account later)
    # make requirements for password
    # check that user name doesn't already exist in the able
    return