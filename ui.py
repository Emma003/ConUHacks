import sys
import csv

registered_cards = []
flight_cost = 0

def main():
    print("GOOD MORNING")

    # Checking for card validity and type
    while(True):
        card_number = input("Kindly enter your rewards card number: ")
        # bool
        is_valid = check_validity(card_number)
        if is_valid:
            card_type = check_type(card_number)
            print("Checking if your " + card_type + " is in our system...")
            break

    if card_in_system(card_number):
        print("Card is in system")
        password = input("Enter password: ")
        if check_password(password):
            print("Welcome to the Sky Club! Here's the main menu:")
            option = input("Please type \n '1' to check your balance \n '2' to submit your flight for reward points "
                           "\n '3' to book a new flight using your reward points \n '4' to EXIT ")
            if option == '1':
                balance = check_balance(card_number)
            elif option == '2' or option == '3':
                flight_id = input("Enter your flight ID: ")
                check_flight(flight_id)
                if check_flight(flight_id) and option == '2':
                    flight_id = input("Enter your flight ID: ")
                    submit_flight(card_number)
                elif check_flight(flight_id) and option == '3':
                    flight_id = input("Enter your flight ID: ")
                    book_flight(card_number)
            elif option == '4':
                print("Come back soon!")


    else:
        print("You do not have an account with us!")
        new_account = input("Would you like to create a new account?")
        if new_account == "Yes" or new_account == "yes":
            create_new_account(card_number)


# returns bool
def check_validity(card_number):
    return True

# returns string
def check_type(card_number):
    return "AMEX"

# returns bool
def card_in_system(card_number):
    return True

#ask for name password and tell em starting balance is $50 or something
def create_new_account(card_number):
    return "null"

#bool. checks password in csv
def check_password(password):
    return True

#returns the balance in the rewards points (in $)
def check_balance(card_number):
    return 0

#checks the user input is valid format (regex) and is in the csv file
def check_flight(flight_code):
    #if flight in file, use global variable flight_cost to store price
    #print flight details
    return 0

#add the value of flight to user balance
def submit_flight(flight_code, card_number):
    return 0

#withdraw the value of flight from user balance, check for insufficient funds
def book_flight(flight_code, card_number):
    return 0

if __name__ == "__main__":
    main()