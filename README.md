# CLUBS TO HIRE
![enter image description here](https://github.com/NigelFinegan5p/project-3/blob/main/images/Clubs_to_Hire_logo_Copy.jpg)

<br></br>
Clubs to Hire was set up in 2010 to give golfers a real alternative with their golf travel needs.

The business model allows users to try out the new models to market and with the convenience of collecting them on arrival at your airport of choice.

So if you are going on a golfing holiday with friends or family or on business, they can save you the hassle of bringing your clubs through busy airport terminals, waiting for them at excess luggage, paying extreme carriage charges and the worry of having them stolen or damaged.

Clubs to Hire offer a variety of sets to suit all standards and tastes. They provide the latest clubs from the top golf manufacturer’s, suitable sized golf bags, friendly service and value for money.

They can arrange to deliver and collect your set from your resort/ accommodation of choice.

The Value/Price proposition is very simple, when visiting the sun-kissed fairways of Portugal, Spain and beyond to the raw beauty of an Irish Links, leave your clubs at home and enjoy the latest in golf club technology.
<p></p>
<p></p>

![enter image description here](https://github.com/NigelFinegan5p/project-3/blob/main/images/CTH_shop.jpg)

<br></br>

## The Story -- Problem/Solution Fit & A Franchise opportunity

![enter image description here](https://github.com/NigelFinegan5p/project-3/blob/main/images/faroshop.jpg)
<p></p>
We have been approached by a potential franchisee to develop an in-house order system as part of their Franchise Model Evaluation.

The client has already conducted significant Market Analysis and has a very good understanding of the local market dynamics where the franchise will operate.

This involved assessing competition, market saturation, and consumer demand within the target location. A detailed market analysis helped them identify the franchise’s viability in the chosen area of Portugal and market and formulate effective marketing and operational strategies.

With a focus on internal stock controls and the ordering optimization we developed a plan with our client for a back end ordering system to assist in inventory management and subsequently financial performance.

<p></p>
<p></p>

![enter image description here](https://github.com/NigelFinegan5p/project-3/blob/main/images/francies-banner-1.jpeg)

<br></br>

 ***UX-End User & Validating user input***

There are many ways to validate input in Python. One of the key objectives of this project was to ensure that the program receives valid and readable input data to avoid problems with the program’s operation and output correctly the price and quantity with customer details, while tracking all orders per programme run. In essence Input validation code checks that values entered by the user, such as text or numeric values from the input () function, and are formatted correctly.


<br></br>


## Scope, build & Technologies
### Language

<p></p>

-   [Python](https://www.python.org/)  is an interpreted, object-oriented, versatile and powerful programming language used for example for web development, machine learning and data science. Python3 was used to create the command line interface for this Golf Clubs ordering system.

### Other Technologies

<p></p>

-   [Github](https://github.com/) were used for version control. Github provides the web interface for the Git code repository.
-   [Gitpod](https://gitpod.io/)  was used as the cloud-based IDE for this project.
-   [Heroku](http://heroku.com/)  is a container-based cloud Platform as a service used to deploy, manage and scale modern applications. Heroku was used to deploy this game application.
-   [The Google Chrome browser](https://www.google.com/intl/en_ie/chrome/)  was used to view the app

<p></p>

<br></br>

## Our code & the why ?

The code below is a simple golf club rental ordering system implemented in Python. It allows users to place orders, choose between pickup or delivery, and view their order details. All processed orders can be viewed by entering the word ***Orders***.

<p></p>

**Imports and Initial Setup**

<p></p>

    import re 
    import sys
Importing the `re` module allows for regular expression operations.
Importing the `sys` module allows access to system-specific parameters and functions.

<p></p>
<p></p>

    MAX_CLUBS = 5 
    DELIVERY_CHARGE = 15
    
MAX_CLUBS = 5: Sets the maximum number of golf club sets that can be ordered in one transaction.

If delivery is selected in the system a DELIVERY_CHARGE = 15: Defines the cost of delivery.


<p></p>
<p></p>

    CLUBS_AVAILABLE = [ 
     {"name": "Titleist", "price": 95},
     {"name": "Taylor Made", "price": 95}, 
     {"name": "Srixon", "price": 85}, 
     {"name": "Callaway", "price": 85}, 
     {"name": "Wilson", "price": 85}, 
     {"name": "Ping", "price": 75}, 
     {"name": "Adams", "price": 75}, ]
     
CLUBS_AVAILABLE: A dictionary list where each dictionary represents a golf club brand and its rental price. Each brand is given a selected number from 1 to 7. For example Adams number 1 and Titleist number 7.

<br></br>

**Function Definitions**

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

`def get_input():` Prompts the user for input and validates it against a regular expression.
`regex`: This module provides regular expression matching operations similar to those found in Perl.
<p></p>

`input_message`: A Prompt message is displayed to the user.<p></p>
`error_message`: An Error message is displayed if the input is invalid.
 


<br></br>

    def print_order(order): 
    print_line("Name: " + order.name) 
    print_line("Order type: " + ("Pickup" if order.pickup else "Delivery")) 
    if not order.pickup: 
       print_line("Delivery address: " + order.address) 
       print_line("Customer phone number: " + order.phone) 
    print_line("") 
    print_line("Order summary:{:15}Price each:{:5}Subtotal:".format("", ""))

<p></p>

Function Definition, This line defines a function named `print_order` that takes a single argument, `order`.
Print the Name, line prints the name of the customer from the `order` object.<p></p>
It uses `order.name` to retrieve the customer's name and concatenates it with the string `"Name: "`. <p></p>
Print Order Type, This line prints the type of order based on the `pickup` attribute of the `order` object. If `order.pickup` is `True`, it prints `"Pickup"`. If `order.pickup` is `False`, it prints `"Delivery"`.<p></p>
Conditional Delivery Information These lines execute only if `order.pickup` is `False`. It prints the delivery address and customer phone number from the `order` object. <p></p>
The `order.address` and `order.phone` attributes are used to fetch and display this information based on the delivery selection.


<br></br>

**Order Class Definition**

    class Order: 
        def __init__(self): 
        self.name = "" 
        self.pickup = False 
        self.address = None 
        self.phone = None 
        self.clubs = [] 
        self.cost = 0

`Order`: A class to represent an order with attributes for the customer's name, order type (pickup or delivery), address, phone number, a list of ordered clubs ( the brand) , and total cost to the customer in euros.


<br></br>

    def get_pickup(self): 
        user_input = get_input( 
            r"[PpDd]", "Pick up or delivery? [Pickup]:", 
            "Please enter a 'p' (pickup) or 'd' (delivery)") 
        if user_input == "CANCEL": 
           return "CANCEL" 
           self.pickup = user_input.lower().startswith("p") or not user_input


`get_pickup()`: Prompts the user (Business owner/franchisee) to choose between pickup or delivery and sets the pickup or delivery attribute accordingly. (Based on web or phone orders)


<br></br>

    def get_name(self): 
        user_input = get_input(r"[A-Za-z]+", "Enter customer name:", 
                               "Name must only contain letters") 
       if user_input == "CANCEL": return "CANCEL" self.name = user_input[:48]

`get_name()`: Prompts the end-user to enter their customers name, ensuring it only contains letters and is truncated to 48 characters only.


<br></br>

        def get_address(self):
        user_input = get_input(
            r"[ -/\w]+", "Delivery address:",
            "Address must only contain alphanumeric characters")
        if user_input == "CANCEL":
            return "CANCEL"
        self.address = user_input[:36]

`get_address()`: Prompts for a delivery address for the customer, allowing alphanumeric characters and certain special characters, and truncates it to 36 characters. Delivery options include Hotel or Apartment complex and within 25 miles of the franchisee branch.


<br></br>

        def get_phone(self):
        user_input = get_input(r"\d+", "Phone number:",
                               "Phone number must only contain numbers")
        if user_input == "CANCEL":
            return "CANCEL"
        self.phone = user_input[:11]
`get_phone()`: Prompts for a phone number, ensuring it only contains digits and is truncated to 11 characters. The inputs it allows are numeric only.


<br></br>

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

`get_clubs()`: Prompts the user to specify the number of club sets they want to order, customer choose from Adams at number 1 to Titleist at number 7. It validates input, and then updates the order with the selected clubs accordingly.


<br></br>

        def get_cost(self):
        self.cost = sum(brand["price"] * brand["amount"] for brand in self.clubs)
        if not self.pickup:
            self.cost += DELIVERY_CHARGE

`get_cost()`: Calculates the total cost of the order based on the price and quantity of each set of club selected, adding the delivery charge if relevant.


<br></br>

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

`get_details()`: Manages the process of collecting all details for an order (pickup or delivery, name, address, phone number, club brand) and calculates the total cost in euros.

<br></br>

**Main Execution Block**

    if __name__ == "__main__":
    print("== Golf Clubs to Hire ==\n"
          "== Club order manager ==\n"
          "Enter 'CCC' to cancel order or 'QQQ' to exit program at any time.\n"
          "To select the Brand of Clubs please choose numbers 1 to 7 (Titleist = 7)\n"
          "The first letter for input are required.\n")

When it runs it checks if the script is being run directly and prints introductory information about the system. As per the above Golf Clubs to Hire etc.


<br></br>

        orders = []
    CLUBS_AVAILABLE = sorted(CLUBS_AVAILABLE, key=lambda k: (k["price"], k["name"]))

The above code Initializes an empty list to store orders and sorts `CLUBS_AVAILABLE` by price and name.

<br></br>

        while True:
        order = Order()
        if order.get_details() != "CANCEL":
            print("\nOrder saved. Order was:")
            print_order(order)
            orders.append(order)
        else:
            print("\nOrder cancelled.")

The main loop to handle order creation. Creates a new `Order` object, collects details, and either saves or cancels the order based on the end user input.


<br></br>


           user_input = get_input(
                r"[YyNnOo]", "Would you like to enter another order or view all previous orders? [Yes]/No/Orders:",
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

Prompts the end user to either place another order, view all previous orders, or exit the program. Displays all previous orders if the user chooses to view them, including all clubs order and total costs associated with the orders.

<br></br>
<br></br>



## Deployment

This application uses Heroku for deployment

**Create the application**

1.  First create the requirements file the Heroku will use to import the dependencies required for deployment: type pip3 freeze > requirements.txt. For this project the requirements.txt file is empty as no libraries or modules were imported other than from the standard python library.
2.  Navigate to the [Heroku](https://www.heroku.com/) website
3.  Create an account by entering your email address and a password
4.  Activate the account through the authentication email sent to your email account
5.  Click the new button and select create a new app from the dropdown menu
6.  Enter a name for the application which must be unique, in this case the app name is project-3p
7.  Select a region, in this case Europe
8.  Click create app

**Heroku settings**

1.  From the horizontal menu bar select 'Settings'.
2.  In the buildpacks section, where further necessary dependencies are installed, click 'add buildpack'. Select 'Python' first and click 'save changes'. Next click 'node.js' and then click 'save changes' again. The 'Python' buildpack must be above the 'node.js' buildpack'. They can be clicked on and dragged to change the order if necessary.


<br></br>



## Testing

**Manual Testing in terminal**

Before stepping into creating tests for our application, we approached this with three basic steps of every test:

1. Create your inputs
2. Execute the code,
3. Capturing the output
4. Compare the output with an expected result
5. Assess output
6. Handle expected failures if needed

<br></br>

| Manual Testing | Details  |
|--|--|
| Pick Up or delivery (Delivery entered) | Pass  |
| Enter Customer Name| Pass |
| Delivery Address| Pass|
| Phone Number | Pass |
|Number of clubs to order| Pass  |
| Enter Brand of clubs you would like to order |Pass|
| Order Saved| Pass  |
| Order Summary with price and delivery locations| Pass  |
|--|--|
| Pick up or delivery (Pick up entered) | Pass  |
| Enter Customer Name | Pass|
| Number of clubs to order| Pass|
| Selection of brand no 1 Adams | Pass |
|Order saved| Pass |
| Order summary with price and delivery | Pass|
|  |  |


<br></br>

**PEP8 Linter**

With a long run Macro view towards writing high-quality, readable Python code by using the guidelines laid out in PEP 8 and tested using the pep8 linter we found the following errors and fixed then accordingly.
<p></p>
With a focus on the guidelines and following them to really improve my project code, and its potential especially when it comes to sharing my portfolio code with potential employers or collaborators in the future.
<p></p>

![enter image description here](https://github.com/NigelFinegan5p/project-3/blob/main/images/pep8.errors.jpg)

<p></p>

![enter image description here](https://github.com/NigelFinegan5p/project-3/blob/main/images/pep8.noerror..jpg)

<br></br>




## Bibliography & Sources

IMPRACTICAL PYTHON PROJECTS, Author Lee Vaughan

[https://www.kea.nu/files/textbooks/humblelearn2code/impracticalpythonprojects.pdf](https://www.kea.nu/files/textbooks/humblelearn2code/impracticalpythonprojects.pdf)


Python Distilled (Developers Library) (1st Edition) (David Beazley)

[https://www.scribd.com/document/764971811/Python-Distilled-Developers-Library-1st-Edition-David-Beazley](https://www.scribd.com/document/764971811/Python-Distilled-Developers-Library-1st-Edition-David-Beazley)

Python for Dummies by Aahz Maruch and Stef Maruch

[https://www.vailtech.net/sites/default/files/Python_Essentials_for_Dummies.pdf](https://www.vailtech.net/sites/default/files/Python_Essentials_for_Dummies.pdf)
