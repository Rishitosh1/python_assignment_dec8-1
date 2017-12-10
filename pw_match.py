def pw_read():
    """this function asks for a password"""
    pw=input("enter password: ")
    return (pw)
def pw_check(pw):
    """function checks whether the entered password matches"""
    if (pw == password):
        print("Password match")
    else:
        print("wrong password")

#defining global static password
password="Password"
#calling function to read and match password
pw=pw_read()
pw_check(pw)
