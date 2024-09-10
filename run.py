'''Golf Clubs to Hire'''
import re
import sys

'''Golf Clubs to Hire Ordering System'''
# Configure ordering system #
# The maximum number of sets of golf clubs per order
MAX_CLUBS = 5
# Delivery charge to Hotel & Apartment != ( price of delviery in € )
DELIVERY_CHARGE = 15
# List of club sets available and price

# top 7 premium brands available in full set offerings, euro € prices #
CLUBS_AVAILABLE = (
    {"name": "Titleist",      "price": 95},
    {"name": "Taylor Made",   "price": 95},
    {"name": "Srixon",        "price": 85},
    {"name": "Callaway",      "price": 85},
    {"name": "Wilson",        "price": 85},
    {"name": "Ping",          "price": 75},
    {"name": "Adams",         "price": 75},
)
# End of configuration and products available


def get_input(regex, input_message=None, error_message=None):
    '''RegEx or regular expression, validate and match input'''
    '''definition of a function and two lines spaces above and below PEP8'''
    while True:
        if input_message:
            user_input = input(str(input_message))
        else:
            user_input = input()
        user_input = user_input.lower().strip()
        # End user UX if user want to cancel the order or quit the order
        if user_input == "qqq" or user_input == "quit":
            sys.exit()
        elif user_input == "ccc" or user_input == "cancel":
            return "CANCEL"

        # check if user input is equal to/ matches the regular expresssion
        if re.match(regex, user_input, re.IGNORECASE):
            break

        # if input does not match with the regular expression,
        # An error message has then been specified
        if error_message:
            print(str(error_message))

    return user_input


def print_line(line):
    '''Prints message used for print order'''
    print("| {:54} |".format(line))


def print_order(order):
    '''Prints the clubs order to the screen'''
    print_line("Name: " + order.name)
    print_line("Order type: " + ("Pickup" if order.pickup else "Delivery"))
    if not order.pickup:
        print_line("Delivery address: " + order.address)
        print_line("Customer phone number" + order.phone)
    print_line("")
    print_line("Order summary:{:15}Price each:{:5}Subtotal:".format("", ""))
    for brand in order.clubs:
        print_line("{:5}x {:22}{:5}€{:5.2f}{:8}€{:>5.2f}".format(
            brand["amount"], brand["name"], "",
            brand["price"], "", brand["price"]*brand["amount"]))
    if not order.pickup:
        print_line("{:4}Delivery charge{:29}€{:>5.2f}".format(
            "", "", DELIVERY_CHARGE))
    
    print_line("{:48}------".format(""))
    print_line("{:40} Total: €{:.2f}".format("", order.cost))


class Order():
  '''Holds the information of each golf clubs order, can got info itself'''
  def __init__(self):
      self.name = ""
      self.pickup = False
      self.address = None
      self.phone = None
      self.clubs = []
      self.cost = 0

  def get_pickup(self):
    user_input = get_input(
        r"€|(?:P|D)",
        "Pick up or delivery? [Pickup]:",
        "Please enter a 'p' (pickup) or 'd' (delivery)")
    if user_input == "CANCEL":
        return "CANCEL"
    self.pickup = user_input.lower().startswith("p") or not user_input

  def get_name(self):
        user_input = get_input(
            r"[A-Z]+€",
            "Enter customer name:",
            "Name must only contain letters")
        if user_input == "CANCEL":
            return "CANCEL"
        self.name = user_input[:48]
  
  
  def get_address(self):
        user_input = get_input(
          r"[ -/\w]+€",
          "Delivery address:",
          "Address must only contain alphanumeric characters")
        if user_input == "CANCEL":
            return "CANCEL"
        self.address = user_input[:36]


  def get_phone(self):
        user_input = get_input(
          r"\d+€",
          "Phone number",
          "Phone number must only contain numbers")
        if user_input == "CANCEL":
          return "CANCEL"
        self.phone = user_input[:11]
        

