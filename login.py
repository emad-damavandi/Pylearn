username = input()
password = input()

if username == "Emad" and password == "006600" :
    print("You have successfuly logged in ✅")
elif username != "Emad" and password != "006600":
    print("Username and password are incorrect!❌")
elif username != "Emad":
    print("Username is incorrect!❌")
elif password != "006600":
    print("Password is incorrect!❌")
else:
    print( "something went wrong!😐")