# Task1: Create user class
# Task2: Add User lacss instance methods
# Task3: Create BankUser subclass
# Task4: Create BankUser class instance methods
# Task5: Transfer and request money
# Bonus 1: Add validation 
#       - only positive numbers can be deposited, withdrawn, transferred, and requested.
#       - if string or negative number is entered:
#           - appropriate message shown
# Bonus 2: update transfer_money() and request_money()
#           - no amount greater than what is available can be transferred
# Bonus 3: validation parameters for the name, password, and PIN
#           and update the change_name(), change_pin(), change_password() methods to enforce those parameters
#           ex.
#               Username can only be changed if:
#                     new name is >= 2 characters && new name <= 10 characters
#                 Password can be changed if:
#                     new password is >= 5
#                 PIN can only be changed if:
#                     new PIN is exactly 4 numbers
#                 the new value cannot be same as the previous value 
#                 no space character are allowed
# Bonus 4: format the output 
#         - dollar amount display 2 digits after the decimal point instead of 1
#         - ex. 500.00 instead of 500.0
# Bonus 5: add an instance attribute on the BankUser class called on_hold and initialize to False
#          add a method that can called to toggle this on_hold class to the opposite of its current Boolean value 
#          if true: flip it to False
#          if false: flip it to True
#          add a check for each of withdraw(), deposit(), transfer_money(), withdraw_money()
#                  if the on_hold attribute for any user involved in the transaction is True,
#                  the transaction is rejected with an appropriate failure message.memoryview
