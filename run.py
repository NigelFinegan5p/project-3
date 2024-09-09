'''Golf Clubs to Hire'''
import re
import sys

'''Golf Clubs to Hire Ordering System'''
#Configure ordering system #
#The maximum number of sets of golf clubs per order
MAX_CLUBS = 5
#Delivery charge to Hotel & Apartment != ( price of delviery in € )
DELIVERY_CHARGE = 15
# List of club sets available and price

CLUBS_AVAILABLE = {
    "Titleist": 95,
    "Taylor Made": 95,
    "Srixon": 85,
    "Callaway": 85,
    "Srixon": 80,
    "Wilson": 80
}
# End of configuration and products available

def get_input(regex, input_message=None, error_message=None):
    '''RegEx or regular expression, validate and match input'''
    while True:
        if input_message:
            user_input = input(str(input_message))
        else:
            user_input = input()
        user_input = user_input.lower().strip()
        # End user UX if user want to cancel the order or quit the order
        if user_input == "qqq" or user_input = "quit":
            sys.exit()
        elif user_input == "ccc" or user_input = "canccel":
            return "CANCEL"

        # check if user input is equal to/ matches the regular expresssion
        if re.match(regex, user_input, re.IGNORECASE):
            break

        # if input does not match with the regular expression,
        # An error message has then been specified
        if error_message:
            print(str(error_message))
            
    return user_input             