def pw_check():
    """this function asks for a password and checks whether it matches the global password"""
    pw=input("enter password: ")
    if(pw == password):
        print("Password match")
    else:
        print("wrong password")
#defining global static password
password="Password"
#calling function to match password
pw_check()