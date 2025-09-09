from colorama.ansi import clear_screen

condition = True
bids = {}
highest_bid = 0
winner = ""

while condition:
    name = input("What is your name?: ")
    pid = float(input("What is your bid?: $"))
    choose = input("Are there any other bidders? (yes/no): ").lower()

    bids[name] = pid
    if choose == "no":
        condition = False

# Find the highest bidder
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print(f"{winner} is the winner with a bid of ${highest_bid}")
