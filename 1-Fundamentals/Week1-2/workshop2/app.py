from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")

# Registeration
# Declare a variable named name, pin by input function
while True:
    name=input("Enter name to register: ")
    
    if len(name)>0 and len(name)<11:
        break            
    elif len(name)>10:
        print("The maximum name length is 10 characters.")
    elif len(name)<=0:
        print("You must enter a name.")
while True:
    pin=input("Enter PIN: ")

    if len(pin)==4:
        break
    else:
        print("PIN must contain only 4 numbers")

# Declare a variable named balance
balance=0.

# echo back the values that were entered using a print statement, and the name and balance variables
# type convert balance to string
print(name,"has been registered with a starting balance of $"+str(balance)+"\n")

# infinite while loop
# requests the user's name and PIN
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")

    name_to_validate=input("Enter name: ")
    pin_to_validate=input("Enter PIN: ")

    if name_to_validate==name and pin_to_validate==pin:
        print("Login successful!\n")
        break
    else:
        print("Invalid credentials!\n")

# infinite while loop
# display the ATM menu 
while True:
    atm_menu(name)

    # Declare a variable named option
    option=input("Choose an option: ")

    if option=='1':
        account.show_balance(balance)
    elif option=='2':
        balance=account.deposit(balance)
        account.show_balance(balance)
    elif option=='3':
        balance=account.withdraw(balance)
        account.show_balance(balance)
    else:
        account.logout(name)
        break




