email="abc@acemail.com"
passw="abc@123"
email_1=input("enter your email= ")
passw_1=input("enter your password= ")
if email==email_1 and passw==passw_1:
    print("you are logged in")
elif email==email_1 and passw!=passw_1:
    print("your password is incorrect")
    passw_2=input("enter your password= ")  
    if passw_2==passw:
        print("yor are logged in")
    else:
        print("rehnede bhai")
else:
    print("out of sylaabbus")             