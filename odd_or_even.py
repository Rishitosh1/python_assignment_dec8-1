#function to check whether the number is odd or even
def check(x):
    if (x%2 == 0):
        print("the number you entered is even")
    else :
        print("the number you entered is odd")
#read input and typecast to integer
x=int(input("enter the number you would like to check "))
#calling function
check(x)
