noofLaptop = input("How many laptop do you have? ")
try:
    if  int(noofLaptop) >= 2:
       print("you are technical guy")
    else:
       print("hmmmm")
except ValueError:
    print("you does not Type a number")
