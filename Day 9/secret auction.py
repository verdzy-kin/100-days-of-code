from Art import logo
print(logo)
bids = {}
Biddingfinished = False

def Highestbidder(biddingrecord):
    Highestbid = 0
    for bidder in biddingrecord:
        bidamnt = biddingrecord[bidder]
        if bidamnt > Highestbid:
            Highestbid = bidamnt
            winner = bidder
    print(f"The winner is {winner} with a bid of ${Highestbid}")

while not Biddingfinished:
    name = input("what is your name?: ")
    price = int(input("what is your bid?: $"))
    bids[name] = price
    shouldcontinue = input("Any other bidders? Type yes or no.\n").lower()
    if shouldcontinue == "no":
        Biddingfinished = True
        Highestbidder(bids)
