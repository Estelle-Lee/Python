def login(database,username,password):
    if username in database:
        if database[username]==password:
            print(f"\nWelcome back {username.upper()}!")
            return username
        else:
            print(f"\nIncorrect password for {username.upper()}")
            return ""
    else:
        print("\nUser not found. Please register")
        return ""

def register(database,username):
    if username in database:
        print("\nUsername already registered\n")
        return ""
    else:
        print(f"\n{username.upper()} Registered successfully\n")
        return username
    
    