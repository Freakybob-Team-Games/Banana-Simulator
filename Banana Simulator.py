
import time
import math
import sys
import random
import threading

print("It's a summer night, you're drunk when one of your friends jokes about a banana business")
time.sleep(3)
print("You then think, 'It might work out'")
time.sleep(2)
print("You walk out the bar and go on your computer")
time.sleep(2)
print("'How to make a profit with bananas'")
time.sleep(2)
print("You start a business and begin your journey")
time.sleep(2)

cash = 50
print("Your current cash is: $" + str(cash))
print("Each banana will cost you 25 cents.")
print("Goal: Get as much cash as possible, don't go bankrupt or sell all your bananas!")
stockmarket = random.uniform(0.10, 0.40)
stockmarket = round(stockmarket, 2)

def generate_random_stock_price():
    while True:
        stockmarket = random.uniform(0.10, 0.40)
        stockmarket = round(stockmarket, 2)
        time.sleep(30)

stock_thread = threading.Thread(target=generate_random_stock_price)
stock_thread.daemon = True
stock_thread.start()


while True:
    try:
        bananns = input("how many bananas do you want? ")
        if bananns == 'uwu':
            print("...")
            time.sleep(2)
            print("You do realize that just because it's from freakybob doesn't mean you have to be freaky")
            time.sleep(4)
            print("Right..?")
            time.sleep(4)
            print("Anyway, go to jail.")
            continue
        bananns = int(bananns)
        break
    except ValueError:
        print("Gtfo now, you failure")

cash = cash - (bananns * 0.25)
if cash < 0:
    print("You already went fucking bankrupt. Nerd.")
    print("You are now: $" + str(cash) + " in debt!")
    sys.exit()
else:
    print("Your cash is now: $" + str(cash))

bananns = int(bananns)
print("Bananas: " + str(bananns))
time.sleep(0.5)
while True:
    menuchoice = input("what are you gonna do now").lower()
    if menuchoice == 'sell':
        try:
            sell = int(input(f"how many sell? (current stock price: {stockmarket})"))
            bananns = bananns - sell
            if bananns < 0:
                print("YOU SOLD MORE THAN YOU HAVE! FRAUD! FRAUD!")
                time.sleep(1)
                print("You're now in jail. Luni is in here too, watch out buddy!")
                sys.exit()
            elif bananns == 0:
                print("You have no bananas anymore. Dang, crazy.")
                print("Game over")
                sys.exit()
            else:
                cash = cash + (sell * stockmarket)
                print("Your cash is now: $" + str(cash))
                print("You now have: " + str(bananns) + " bananas!")
        except ValueError:
            print("CRITICAL EXCEPTION! bananas invalid :(")
    if menuchoice == 'stocks':
        print("Current stocks are: " + str(stockmarket) + " per banana!")
    if menuchoice == 'buy':
        try:
            buy = int(input(f"buy how many bananas? (current stock price: {stockmarket})"))
            cash -= (buy * stockmarket)
            bananns += buy
            if cash < 0:
                print("You went broke, your wife left you because of this")
                sys.exit()
            else:
                print("Your cash is now: $" + str(cash))
                print("You now have: " + str(bananns) + " bananas!")
        except ValueError:
            print("CRITICAL EXCEPTION! bananas invalid :(")
    if menuchoice == 'rodrick':
        print("Rodrick took 10% of your bananas.")
        bananns = (90 / 100) * bananns
        bananns = round(bananns)
        print("Your bananas are now: " + str(bananns))