from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login,register

database={"admin":"password123"}
donations=[]
authorized_user=""

while True:
    show_homepage()
    if authorized_user=="":
        print("You must be logged in to donate")
    else:
        print(f"Logged in as: {authorized_user}")

# Task3: handle user input

    user_option=input("Choose your option: ")

    if user_option=='1':    # login
        username=input("\nEnter your username: ").lower()
        password=input("Enter your password: ").lower()
        authorized_user=login(database,username,password)
    elif user_option=='2':  # register
        while True:
            username=input("\nEnter your username: ").lower()
            if len(username)>10:
                print("Username should not exceed 10 characters. \nTry again :)")
            else:
                break

        while True:
            password=input("Enter your password: ").lower()
            if len(password)<5:
                print("Password should contain at least 5 characters.\nTry agin! ;)")
            else:
                break

        authorized_user=register(database,username)
        if authorized_user!="":
            database[username]=password
    elif user_option=='3':  # donate
        if authorized_user=="":
            print("\nYou are not logged in\n")
        else:
            donation_string=donate(username)
            donations.append(donation_string)
    elif user_option=='4':  # show donations
        show_donations(donations)
    elif user_option=='5':  # exit
        print("Goodbye")
        break
    else:
        print("Invalid input")


        

