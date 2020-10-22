import random
import sqlite3
import os.path


#OBJECT CARD
class card:
    
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = 0

    def __hash__(self):
        return hash((self.number, self.pin))

    def __eq__(self, other):
        return self.number == other.number and self.pin == other.pin

accounts = set()

#exitsDB = False
if (os.path.exists('card.s3db')):
    exitsDB = True

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

#CREATE TABLE IF NOT EXITST 
cur.execute('CREATE TABLE IF NOT EXISTS card ( id INTEGER PRIMARY KEY AUTOINCREMENT, number VARCHAR(20) NOT NULL, pin VARCHAR(4), balance INT DEFAULT(0)); ')
conn.commit()

#CHECK IF THE CARD NUMBER AND PIN ARE CORRECTS
def luhnAlgorithm(cardNumber):
    sumAll = 0
    for index in range(0, 15):
        value = int(cardNumber[index])
        if ((index + 1) % 2) != 0:
            value = value * 2

        if value > 9:
            value -= 9

        sumAll += value

    checksum = 0
    while ((sumAll + checksum) % 10) != 0:
        checksum += 1
    return str(checksum)


def addToDataBase(newCard):
    cur.execute("INSERT INTO card (number, pin) VALUES ( '{}', '{}');".format(newCard.number, newCard.pin))
    conn.commit()
    
def createAccount():

    while True:

        #Generate card number
        newNumber = "400000"
        acoutnId = str(random.randrange(0,999999999))
        while len(acoutnId) < 9:
            acoutnId = "0" + acoutnId
        newNumber += acoutnId 
        newNumber += luhnAlgorithm(newNumber)
      
        #Generate card pin
        newPin = str(random.randrange(0,9999))
        while len(newPin) < 4:
            newPin = "0" + newPin

        #Create card whith new data
        cardNew = card(newNumber, newPin)

        #Check if this account number already exist
        #if cardNew not in bank:
        print("Your card has been created")
        print("Your card number:")
        print(cardNew.number)
        print("Your card PIN:")
        print(cardNew.pin)
        addToDataBase(cardNew)
        break
    print() 

def logIntoAccount():
    cardAux = card(input("Enter your card number:\n"), input("Enter your PIN:\n"))
    
    cur.execute("select * from card where number={} and pin={};".format(cardAux.number, cardAux.pin))
    #print(len(cur.fetchall()))

    if len(cur.fetchall()) == 0:
        print("\nWrong card number or PIN!\n")
    else:
        print("\nYou have successfully logged in!")
        while(True):
            
            optionLog = input("\n1. Balance\n2. Log out\n0. Exit\n")
            print()

            if optionLog == '1':          # Balance
                cur.execute("select balance from card where number={} and pin={};".format(cardAux.number, cardAux.pin))
                outputBD = cur.fetchone()
                print("Balance: " + str(outputBD[0]))
            elif optionLog == '2':        # Log Out
                print("You have successfully logged out!")
                break
            elif optionLog == '0':
                conn.close()
                exit()
        print()

while True:
    print
    option = input("1. Create an account\n2. Log into account\n0. Exit\n")
    print()
    if option == '1':     # create an account
        createAccount()
    elif option == '2':     # Log into account
        logIntoAccount()
    elif option == '0':     # Exit
        conn.close()
        print ("Bye!")
        break
    

