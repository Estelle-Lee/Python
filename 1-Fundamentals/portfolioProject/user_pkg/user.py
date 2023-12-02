def register(database,username):
    if username in database:
        print("\nPlayer already registered\n")
        return ""
    else:
        print(f"\n{username.upper()} Registered successfully\n")
        return username
    
    