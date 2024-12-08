import time
import random
import threading
import json
file = open('F.json', 'r+')
data = json.load(file)
def end():
    raise SystemExit

# print("It's a summer night, you're drunk when one of your friends jokes about a banana business")
# time.sleep(3)
# print("You then think, 'It might work out'")
# time.sleep(2)
# print("You walk out the bar and go on your computer")
# time.sleep(2)
# print("'How to make a profit with bananas'")
# time.sleep(2)
# print("You start a business and begin your journey")
# time.sleep(2)

cash = 50
print("Your current cash is: $" + str(cash))
print("Each banana will cost you 25 cents.")
print("Goal: Get as much cash as possible, don't go bankrupt or sell all your bananas!")
stockmarket = round(random.uniform(0.10, 0.40), 2)
day = 0 

def generate_random_stock_price():
    global stockmarket
    while True:
        stockmarket = round(random.uniform(0.10, 0.40), 2)
        time.sleep(30)
        
def day_system():
    global day
    while True:
        day += 1
        print(f" Day {day}")
        time.sleep(random.randint(120,180))

stock_thread = threading.Thread(target=generate_random_stock_price)
stock_thread.daemon = True
stock_thread.start()

day_thread = threading.Thread(target=day_system)
day_thread.daemon = True
day_thread.start()

while True:
    try:
        bananns = input("how many bananas do you want? \n")
        if bananns == 'uwu' or "~" in bananns:
            print("...")
            time.sleep(2)
            print("You do realize that just because it's from freakybob doesn't mean you have to be freaky")
            time.sleep(4)
            print("Right..?")
            time.sleep(4)
            print("Anyway, go to jail.")
            end()
        bananns = int(bananns)
        data['bananas'] = str(bananns)
        # data.update({"bananas": bananns}) | this works, but doesn't add "quotes" around the number
        with open('F.json', 'w') as JSONFile:
            json.dump(data, JSONFile, ensure_ascii=False, indent=4)
        break
    except ValueError:
        print("Gtfo now, you failure (ValueError)")

cash -= (bananns * 0.25)
if cash < 0:
    print("You already went fucking bankrupt. Nerd.")
    print("You are now: $" + str(cash) + " in debt!")
    end()
else:
    print("Your cash is now: $" + str(cash))

print("Bananas: " + str(bananns))
time.sleep(0.5)
while True:
    menuchoice = input("what are you gonna do now\n").lower()
    if menuchoice == 'sell':
        try:
            sell = int(input(f"how many sell? (current stock price: {stockmarket})\n"))
            bananns -= sell
            if bananns < 0:
                print("YOU SOLD MORE THAN YOU HAVE! FRAUD! FRAUD!")
                time.sleep(1)
                print("You're now in jail. Luni is in here too, watch out buddy!")
                end()
            elif bananns == 0:
                print("You have no bananas anymore. Dang, crazy.")
                print("Game over")
                data['bananas'] = 0
                end()
            else:
                cash += (sell * stockmarket)
                print("Your cash is now: $" + str(cash))
                print("You now have: " + str(bananns) + " bananas!")
        except ValueError:
            print("CRITICAL EXCEPTION! bananas invalid :(")
    elif menuchoice == 'stocks':
        print("Current stocks are: " + str(stockmarket) + " per banana!\n")
    elif menuchoice == 'buy':
        try:
            buy = int(input(f"buy how many bananas? (current stock price: {stockmarket})\n"))
            cash -= (buy * stockmarket)
            bananns += buy
            if cash < 0:
                print("You went broke, your wife left you because of this")
                end()
            else:
                print("Your cash is now: $" + str(cash))
                print("You now have: " + str(bananns) + " bananas!")
                data['bananas'] = bananns
        except ValueError:
            print("CRITICAL EXCEPTION! bananas invalid :(")
    elif menuchoice == 'rodrick':
        print("Rodrick took 10% of your bananas.")
        bananns = round(bananns * 0.9)
        print("Your bananas are now: " + str(bananns))
