# parameter: balance
# Display: account balance of the logged-in user
def show_balance(balance):
    print("Current balance is: "+str(balance))

# parameter: balance
# variable: amount
# return: balance
def deposit(balance):
    amount=float(input("Enter amount to deposit: "))

    # adding the balance
    balance=balance+amount

    # return adding the balance
    return balance

# parameter: balance
# variable: amount
# return: balance
def withdraw(balance):
    while True:
        amount=float(input("Enter amount to withdraw: "))

        if amount<=balance:
            # subtract the amount from the balance
            balance=balance-amount
            break
        else:
            print("Invalid amount to withdraw.")
            return balance

    

    # return the balance
    return balance

# parameter: name
def logout(name):
    print("Goodbye",name)