marks = int(input("Please enter your marks: "))

if 70 < marks <= 100:
    print("You have scored an A grade")
elif 60 <= marks < 70:
    print("You have scored a B grade")
elif 50 <= marks < 60:
    print("You have scored a C grade")
elif 40 <= marks < 50:
    print("You have scored a D grade")
elif 0 <= marks < 40:
    print("You have scored an E")
else:
    print("Invalid marks entered")