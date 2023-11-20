total_donation=0.

def show_homepage():
    print("        === DonateMe Homepage ===      ")
    print("---------------------------------------")
    print("| 1. Login        | 2. Register        |")
    print("---------------------------------------")
    print("| 3. Donate       | 4. Show Donations  |")
    print("---------------------------------------")
    print("|              5. Exit                 |")
    print("---------------------------------------")

def donate(username):
    """I want to use type() or .isdigit() and else to exclude
        but mostly, I am thinking of try-except
        so that when user insert their input, 
        immediately change it's type to float
        as below:
        donation_amt=float(input("Enter:"))
        and so if user input alphabet or something else instead of digit,
        system automatically display error.
        I want to know if I can except or catch that string error to 
        print out the message and exit the system.
        and if it's digit, continue
        """
    while True:
        donation_amt=input("\nEnter amount to donate: ")
        # when user input string like alphabet, exit the system
        # if user input 0: print invalid input and try again
        # if user input negative value: print invalid input and try again
        if float(donation_amt):
            donation_amt=float(donation_amt)
            if donation_amt==0 or donation_amt<0:
                print("\nInvalid input. Please input positive numeric amount.\n")
            else:
                break
        else:
            print("\nInvalid input. \nNumeric amount only please.\n")
    donation_string=f"{username} donated ${donation_amt}"
    print("Thank you for your donation\n")
    total_donation+=donation_amt
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations)==0:
        print("\nCurrently, there are no donations\n")
    else:
        for donation in donations:
            print(donation)
    print(f"Total = ${total_donation}")
