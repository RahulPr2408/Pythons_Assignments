phoneNumber = input("Enter phone number : ")

valid = False
if len(phoneNumber) == 12 and phoneNumber[3] == '-' and phoneNumber[7] == '-':
    if (phoneNumber[0:3] + phoneNumber[4:7] + phoneNumber[8:]).isdigit():
        valid = True

if valid:
    print(phoneNumber," is valid...");
else:
    print(phoneNumber," is not valid!!!")