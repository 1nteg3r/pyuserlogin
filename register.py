username = input("Enter an username ")
password = input("Enter a password ")
repeat_password = input("Repeat your password ")
while password != repeat_password:
    print("Wrong password. Try again!")
    repeat_password = input("Repeat your password ")
else:
    print(f"Welcome {username}! ")
