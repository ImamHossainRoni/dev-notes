year = input("Enter year :")
year = int(year)
if year%4 != 0:
    print("Not leap year")
else:
    if year % 100 == 0:
        if year %400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    print("Yeas leap year")
