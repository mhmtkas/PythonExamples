userList = []
for i in range(4):
    if i==0:
        userList.append(input("First Name: "))
    elif i==1:
        userList.append(input("Last Name: "))
    elif i==2:
        userList.append(int(input("Age: ")))
    else:
        userList.append(int(input("Date of Birth (Year): ")))

for  i in range(4):
    print(userList[i])

if userList[2] < 0:
    print("\nInvalid Value for Age")
else:
    if userList[2] < 18:
        print("\nYou can't go out because it's too dangerous.")
    else:
        print("\nYou can go out to the street.")

input()  #for waiting in cmd screen


