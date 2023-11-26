# Python Fundamentals - Week4 workshop
# Date: 25/11/2023
# Author: Bokyung Lee

class User:
    def __init__(self,name,pin,password):
        self.name=name
        self.pin=pin
        self.password=password

    # changes the name of the user
    # parameter -   new_name:string
    # return -  None
    def change_name(self,new_name):
        if self.name!=new_name:
            if ' ' not in new_name:
                if len(new_name)>=2 and len(new_name)<=10:
                    self.name=new_name
                else:
                    print("Username should have length of 2-10 characters.")
            else:
                print("No space characters are allowed")
        else:
            print("Invalid change: You cannot use previous UserName")
        
    # changes the pin of the user
    # parameter -   new_pin:integer
    # return -  None
    def change_pin(self,new_pin):
        if ' ' in str(new_pin):
            print("No space characters are allowed")
        elif len(str(new_pin))!=4:
            print("PIN should have 4 numbers only")
        else:
            try:
                if self.pin == int(new_pin):
                    print("Invalid change: You cannot use previous PIN\n")
                else:
                    self.pin=int(new_pin)
            except TypeError:
                print("PIN should be integer\n")           
        

    # changes the password of the user
    # parameter -   new_password:string
    # return -  None
    def change_password(self,new_password):
        if self.password!=new_password:
            if ' ' in new_password:
                print("No space characters are allowed")
            else:
                if len(new_password)>=5:
                    self.password=new_password
                else:
                    print("Password should have more than 4 characters")
        else:
            print("Invalid change: You cannot use previous password")

class BankUser(User):
    def __init__(self,name,pin,password):
        super().__init__(name,pin,password)
        self.balance=0
        self.on_hold=False

    # toggle whether is hold to unhold. Unhold to hold.
    # return -  None
    def toggle_hold(self):
        is_hold=self.on_hold
        if is_hold:
            self.on_hold=False
        else:
            self.on_hold=True


    # prints the bankuser object's balance
    # return -  None
    def show_balance(self):
        balance=str(self.balance)
        print(f"{self.name} has an account balance of: {balance}")

    # withdraws money, decreases the account balance
    # parameter -   amount:value
    # return -   boolean
    def withdraw(self,amount):
        # if account is hold
        if self.on_hold:
            print(f"\nTransaction is rejected.\n{self.name}'s account is currently on hold.\n")
            return False
        
        # if account is not hold
        try:
            amount=float(amount)
            if amount<0:
                print("Invalid amount.")
                return False
            elif amount>self.balance:
                print("Failed. Not available amount")
                return False
            else:
                self.balance -= amount
                return True
        except ValueError:
            # if amount is not a numeric value
            print("Invalid value type. Amount should be numeric value")
            return False     

    # deposits money, increases the account balance
    # parameter -   amount:value
    # return -  boolean
    def deposit(self,amount):
        # if account is hold
        if self.on_hold:
            print(f"\nTransaction is rejected.\n{self.name}'s account is currently on hold.\n")
            return False
        
        # if account is not hold
        try:
            amount=float(amount)
            if amount<0:
                print("Invalid amount of money")
                return False
            self.balance += amount
            return True
        except ValueError:
            # if amount is not a numeric value
            print("Invalid value type. Amount should be numeric value")
            return False

    # Transfer money to another user 
    # parameter -   user:Object, amount:value
    # return -  boolean
    def transfer_money(self,user,amount):
        # if account is hold
        if self.on_hold:
            print(f"\nTransaction is rejected.\n{self.name}'s account is currently on hold.\n")
            return False
        if user.on_hold:
            print(f"\nTransaction is rejected.\n{user.name}'s account is currently on hold.\n")
            return False
        
        # if account is not hold
        try:
            if amount<0:
                print("Invalid amount: Negative value")
                return False
            
            format_float="{:.2f}".format(amount)
            print(f"You are transferring ${format_float} to {user.name}")
            print("\nAuthentication required\n")
            my_pin=int(input(f"Enter {self.name}'s PIN:"))
            if my_pin!=self.pin:
                print("Invalid PIN. Transaction canceled.")
                return False
                
            print("\nTransfer authorized\n")
            print(f"Transferring ${format_float} to {user.name}")
        except ValueError:
            print("Value Error. Failed to transfer\n")
            return False
        except TypeError:
            print("Type Error. Failed to transfer\n")
            return False
        # self.balance-=amount
        # user.balance+=amount
        
        transferred=self.withdraw(amount)
        if transferred:
            user.deposit(amount)
            print("Transferred Successfully!\n")
            return True
        else:
            return False
                

    # Ask for the pin for the user receiving the request for money
    # if credentials are correct
    # parameter -   user:Object, amount:value
    # return -  boolean 
    def request_money(self,user,amount):
        # if account is hold
        if self.on_hold:
            print(f"\nTransaction is rejected.\n{self.name}'s account is currently on hold.\n")
            return False
        if user.on_hold:
            print(f"\nTransaction is rejected.\n{user.name}'s account is currently on hold.\n")
            return False
            
        # if account is not hold
        try:
            if amount<0:
                print("Invalid amount: Negative value")
                return False
        
            format_float="{:.2f}".format(amount)
            print(f"You are requesting ${format_float} from {user.name}")
            print("\nUser authentication is required...\n")

            user_pin=int(input(f"Enter {user.name}'s PIN:"))
            if user_pin != user.pin:
                print("Invalid PIN. Transaction canceled.")
                return False
            
            my_password=input(f"Enter {self.name}'s password:")
            if my_password != self.password:
                print(f"Invalid password. Transaction canceled.")
                return False
            
            print("\nRequest authorised\n")

            requested=user.withdraw(amount)
            if requested:
                self.deposit(amount)
                print(f"{user.name} sent ${format_float}")
                return True
            else:
                return False
        except ValueError:
            print("Value Error. Fail to request\n")
            return False
        except TypeError:
            print("Type Error. Fail to request\n")
            return False


            

print('"""Driver Code for Bonus Task"""')
user1=BankUser("Bob",1234,"bobpassword")
user2=BankUser("Alice",2345,"alicepassword")
user3=BankUser("Estelle",3456,"estellepassword")

print('\n == Bonus Task 1-2 == ')
user1.deposit(5000)  # Processed successfully
user2.deposit('five thousand')  # failed. wrong parameter type
user3.deposit(-500) # failed. negative value
user1.show_balance()
user2.show_balance()
user3.show_balance()
print()
user1.withdraw(10000)    # failed. unavailable transaction amount
user2.withdraw('one hundred')   # failed. wrong parameter type
user3.withdraw(0)   # Processed
user1.show_balance()
user2.show_balance()
user3.show_balance()
print()
user1.transfer_money(user2,500) # Processed
user2.transfer_money(user3,500) # Processed
user3.transfer_money(user1,1000)    # failed. unavailable amount
user1.transfer_money(user2,'amount')    # failed. wrong parameter type
user1.show_balance()
user2.show_balance()
user3.show_balance()
print()
user2.request_money(user1,1000) # Processed
user3.request_money(user2,-1000) # failed. wrong amount
user1.request_money(user3,'amount') # failed. wrong parameter
user1.show_balance()
user2.show_balance()
user3.show_balance()
print()

print('\n == Bonus Task 3-4 == ')
user1.change_name('bob bob bob')    # invalid space
user2.change_password('alicepassword')  # same password - failed
user3.change_pin(0) # invalid length of pin
user1.change_pin(0000)  # processed
user2.change_password('pwd2345')    #processed
user3.change_name('Anne-marie') #processed
print('format dollar amounts with 2 digits: "{:.2f}".format(amount)')

print('\n == Bonus Task 5 == ')
# switch user1's boolean value to True
print("Hold" if user1.toggle_hold() else "Un Hold")
user1.show_balance()
user1.deposit(300)
user1.transfer_money(user2,300)
user1.request_money(user2,100)
user2.request_money(user1,100)

        
    
""" Driver Code for Task 5"""
# bankuser1=BankUser("Bob",1234,"password")
# bankuser2=BankUser("Alice",4321,"alicePassword")
# bankuser2.deposit(5000)
# bankuser2.show_balance()
# bankuser1.show_balance()
# print()

# bankuser2.transfer_money(bankuser1,500)
# bankuser2.show_balance()
# bankuser1.show_balance()
# print()

# bankuser2.request_money(bankuser1,250)
# bankuser2.show_balance()
# bankuser1.show_balance()



""" Driver Code for Task 4"""
# bankuser1=BankUser("Bob",1234,"password")
# bankuser1.show_balance()
# bankuser1.deposit(1000)
# bankuser1.show_balance()
# bankuser1.withdraw(500)
# bankuser1.show_balance()

""" Driver Code for Task 3"""
# bankuser1=BankUser("Bob",1234,"password")
# print(bankuser1.name,bankuser1.pin,bankuser1.password,bankuser1.balance)

""" Driver Code for Task 2 """
# user1=User("Bob",1234,"password")
# print(user1.name,user1.pin,user1.password)
# user1.change_name(new_name="Bobby")
# user1.change_pin(new_pin="4321")
# user1.change_password(new_password="newpassword")
# print(user1.name,user1.pin,user1.password)

""" Driver Code for Task 1 """
# user1=User("name":"Bob","pin":1234,"password":"password")
# print(user1.name,user1.pin,user1.password)