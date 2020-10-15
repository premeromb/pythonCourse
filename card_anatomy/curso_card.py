
class card:
    
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = 0

    def __hash__(self):
        return hash((self.number, self.pin))

    def __eq__(self, other):
        return self.number == other.number and self.pin == other.pin


bank = set()
bank.add(card("666", "222"))

if card("666", "111") in bank:
    print("ESTA!") 

def createAccount():
    
    while True:

        #Generate card number
      
        #Generate card pin
     
        #Create card whith new data
        carNew = card("444","909")

        #Check if this account number already exist
        if carNew not in bank:
            print("Your card has been created")
            print("Your card number:")
            print(carNew.number)
            print("Your card PIN:")
            print(carNew.pin)
            bank.add(carNew)
            break
    print() 

def logIntoAccount():
    
    cardAux = card(input("Enter your card number:\n"), input("Enter your PIN:\n"))

    if cardAux not in bank:
        print("\nWrong card number or PIN!")
    else:
        print("\nYou have successfully logged in!")
        while(True):
            
            optionLog = input("\n1. Balance\n2. Log out\n0. Exit\n")
            print()

            if optionLog == '1':          # Balance
                print("Balance: " + str(cardAux.balance))
            elif optionLog == '2':        # Log Out
                print("You have successfully logged out!")
                break
            elif optionLog == '0':
                break
        print()

while True:
    option = input("1. Create an account\n2. Log into account\n0. Exit\n")
    print()
    if option == '1':     # create an account
        createAccount()
    elif option == '2':     # Log into account
        logIntoAccount()
    elif option == '0':     # Exit
        print ("Bye!")
        break
    

