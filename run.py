import re
import sys
'''Golf Clubs to Hire Ordering System'''
# Configure ordering system #
# The maximum number of sets of golf clubs per order
MAX_CLUBS = 5
DELIVERY_CHARGE = 15
# top 7 premium brands available in full set offerings, euro € prices #
CLUBS_AVAILABLE = [
    {"name": "Titleist", "price": 95},
    {"name": "Taylor Made", "price": 95},
    {"name": "Srixon", "price": 85},
    {"name": "Callaway", "price": 85},
    {"name": "Wilson", "price": 85},
    {"name": "Ping", "price": 75},
    {"name": "Adams", "price": 75},
]


def get_input(regex, input_message=None, error_message=None):
    while True:
        if input_message:
            user_input = input(str(input_message))
        else:
            user_input = input()
        user_input = user_input.lower().strip()
        if user_input in ["qqq", "quit"]:
            sys.exit()
        elif user_input in ["ccc", "cancel"]:
            return "CANCEL"
        if re.match(regex, user_input, re.IGNORECASE):
            break
        if error_message:
            print(str(error_message))
    return user_input


def print_line(line):
    print("| {:54} |".format(line))


def print_order(order):
    print_line("Name: " + order.name)
    print_line("Order type: " + ("Pickup" if order.pickup else "Delivery"))
    if not order.pickup:
        print_line("Delivery address: " + order.address)
        print_line("Customer phone number: " + order.phone)
    print_line("")
    print_line("Order summary:{:15}Price each:{:5}Subtotal:".format("", ""))
    for brand in order.clubs:
        print_line("{:5}x {:22}{:5}€{:5.2f}{:8}€{:>5.2f}".format(
            brand["amount"], brand["name"], "", brand["price"], "",
            brand["price"] * brand["amount"]))
    if not order.pickup:
        print_line("{:4}Delivery charge{:29}€{:>5.2f}".format(
            "", "", DELIVERY_CHARGE))
    print_line("{:48}------".format(""))
    print_line("{:40} Total: €{:.2f}".format("", order.cost))


class Order:
    def __init__(self):
        self.name = ""
        self.pickup = False
        self.address = None
        self.phone = None
        self.clubs = []
        self.cost = 0

    def get_pickup(self):
        user_input = get_input(
            r"[PpDd]", "Pick up or delivery? [Pickup]:",
            "Please enter a 'p' (pickup) or 'd' (delivery)")
        if user_input == "CANCEL":
            return "CANCEL"
        self.pickup = user_input.lower().startswith("p") or not user_input

    def get_name(self):
        user_input = get_input(r"[A-Za-z]+", "Enter customer name:",
                               "Name must only contain letters")
        if user_input == "CANCEL":
            return "CANCEL"
        self.name = user_input[:48]

    def get_address(self):
        user_input = get_input(
            r"[ -/\w]+", "Delivery address:",
            "Address must only contain alphanumeric characters")
        if user_input == "CANCEL":
            return "CANCEL"
        self.address = user_input[:36]

    def get_phone(self):
        user_input = get_input(r"\d+", "Phone number:",
                               "Phone number must only contain numbers")
        if user_input == "CANCEL":
            return "CANCEL"
        self.phone = user_input[:11]

    def get_clubs(self):
        while True:
            user_input = get_input(r"\d+", "Number of clubs to order:",
                                   "Must be a digit, 5 or less")
            if user_input == "CANCEL":
                return "CANCEL"
            if 0 < int(user_input) <= MAX_CLUBS:
                number_clubs = int(user_input)
                break
            else:
                print("Must be a digit, 5 or less (but more than 0)")

        print("\nWhat clubs would you like to order?")
        for i, brand in enumerate(CLUBS_AVAILABLE):
            print("{}: {}".format(str(i + 1).zfill(2), brand["name"]))

        print("\nEnter your selection number for clubs you want to order")
        for i in range(number_clubs):
            while True:
                user_input = get_input(
                    r"\d+", "Brand #{} of {}:".format(i + 1, number_clubs),
                    "Brand selection number must "
                    "correspond to those listed above")
                if user_input == "CANCEL":
                    return "CANCEL"
                try:
                    if int(user_input) == 0:
                        raise IndexError
                    to_add = CLUBS_AVAILABLE[int(user_input) - 1]
                except IndexError:
                    print("Brand selection number must "
                          "correspond to those listed above")
                else:
                    break

            for ordered in self.clubs:
                if to_add["name"] == ordered["name"]:
                    ordered["amount"] += 1
                    break
            else:
                to_add["amount"] = 1
                self.clubs.append(to_add)

    def get_cost(self):
        self.cost = sum(brand["price"] *
                        brand["amount"] for brand in self.clubs)
        if not self.pickup:
            self.cost += DELIVERY_CHARGE

    def get_details(self):
        if self.get_pickup() == "CANCEL":
            return "CANCEL"
        if self.get_name() == "CANCEL":
            return "CANCEL"
        if not self.pickup:
            if self.get_address() == "CANCEL":
                return "CANCEL"
            if self.get_phone() == "CANCEL":
                return "CANCEL"
        if self.get_clubs() == "CANCEL":
            return "CANCEL"
        self.get_cost()


if __name__ == "__main__":
    print("== Golf Clubs to Hire ==\n"
          "== Club order manager ==\n"
          "Enter 'CCC' to cancel order or 'QQQ' to exit program at any time.\n"
          "To select the Brand of Clubs please choose:\
           Numbers 1 to 7 (Titleist = 7)\n"
          "The first letter for input are required.\n")

    orders = []
    CLUBS_AVAILABLE = sorted(CLUBS_AVAILABLE,
                             key=lambda k: (k["price"], k["name"]))

    while True:
        order = Order()
        if order.get_details() != "CANCEL":
            print("\nOrder saved. Order was:")
            print_order(order)
            orders.append(order)
        else:
            print("\nOrder cancelled.")

        user_input = get_input(
            r"[YyNnOo]", "Would you like to enter another order \
            or view all previous orders? [Yes]/No/Orders:",
            "Only yes/no or \"orders\" responses allowed")
        if user_input.lower().startswith("n"):
            sys.exit()
        elif user_input.lower().startswith("o"):
            for i, order in enumerate(orders):
                if i == 0:
                    print("-" * 23 + " ALL ORDERS " + "-" * 23)
                else:
                    print("|" + "-" * 56 + "|")
                print_order(order)
                if i == len(orders) - 1:
                    print("-" * 58)
