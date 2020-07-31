#  [water, milk, coffee, costs]
espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappuccino = [200, 100, 12, 6]


class CofeeMachine:

    num_machine = 0
    state = "initial" # ["initial", "buy", "fill"]
    state_fill = 0 # [0, 1, 2, 3]
    info = espresso[:]

    def __init__(self, water, milk, coffee_beans, cups, money):

        self.total_water = int(water)
        self.total_milk = milk
        self.total_coffee_beans = coffee_beans
        self.total_cups = cups
        self.total_money = money
        self.total_info = None

    def __new__(cls, water, milk, coffee_beans, cups, money):
        if cls.num_machine == 0:
            cls.num_machine += 1
            return object.__new__(cls)
        return None


    def enaught_products(self, info_list):

        if (self.total_water - info_list[0]) < 0:
            print("Sorry, not enough water!")
        elif (self.total_milk - info_list[1]) < 0:
            print("Sorry, not enough milk!")
        elif (self.total_coffee_beans - info_list[2]) < 0:
            print("Sorry, not enough cofee beans!")
        elif (self.total_cups - 1) < 0:
            print("Sorry, not enough disposable cups!")
        else:
            return True
            
        return False

    def buy(self, buy_option):  

        if buy_option == '1':
            info = espresso[:]
        elif buy_option == '2':
            info = latte[:]
        elif buy_option == '3':
            info = cappuccino[:]

        if buy_option != 'back' and self.enaught_products(info): 
            print("I have enough resources, making you a coffee!")   
            self.total_water -= info[0]
            self.total_milk -= info[1]
            self.total_coffee_beans -= info[2]
            self.total_money += info[3]
            self.total_cups -= 1

    def fill(self, fill_amount):
        if self.state_fill == 0:
            self.total_water = self.total_water + int(fill_amount)
        elif self.state_fill == 1:
            self.total_milk += int(fill_amount)
        elif self.state_fill == 2:
            self.total_coffee_beans += int(fill_amount)
        elif self.state_fill == 3:
            self.total_cups += int(fill_amount)
            self.state = "initial"
        
        if self.state_fill == 3:
            self.state_fill = 0
        else:
            self.state_fill += 1


    def take(self):
        print("")
        print("I gave you ${}".format(self.total_money))
        self.total_money = 0

    def remaining(self):
        print("\nThe coffee machine has:")
        print("{} of water".format(self.total_water))
        print("{} of milk".format(self.total_milk))
        print("{} of coffee beans".format(self.total_coffee_beans))
        print("{} of disposable cups".format(self.total_cups))
        print("{} of money".format(self.total_money))


    def console_read(self, read):
        if self.state == "initial":
            if read == "buy":
                print("\nWhat kind of coffie do you want? (1 - espresso, 2 - latte, 3 - cappuccino), back - to main menu: ")
                self.state = "buy"   
            if read == "fill":
                print("\nWrite how many ml of water do you want to add: ")
                self.state = "fill"
            if read == "take":
                self.take()
            if read == "remaining":
                self.remaining()

        elif self.state == "buy":
            self.buy(read)
            self.state = "initial"

        elif self.state == "fill":
            if self.state_fill == 0:
                print("Write how many ml of milk do you want to add: ")
            elif self.state_fill == 1:
                print("Write how many grams of coffee beans do you want to add: ")
            elif self.state_fill == 2:
                print("Write how many disposable cups of coffee do you want to add: ")    

            self.fill(read)


CM = CofeeMachine(400, 540, 120, 9, 550)
# (self, water, milk, coffee_beans, cups, money):

while True:
    if CM.state == "initial":
        print("\nWrite action (buy, fill, take, remaining, exit):")
    taken = input()
    if taken == "exit":
        break
    CM.console_read(taken)


