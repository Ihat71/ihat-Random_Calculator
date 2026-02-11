#new project
import re
x = input("Enter your credit card number: ")
if re.search(r"^[3]([47])[0-9]{13}$", x):
    print("AMEX")
elif re.search(r"^[5]([1-5])[0-9]{14}$", x):
    print("Mastercard")
elif re.search(r"^[4][0-9]{12}([0-9]{3})?$", x):
    print("VISA")
else:
    print("Invalid")
