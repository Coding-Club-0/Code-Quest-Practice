cases = int(input().rstrip())

def calculateTotal(cards):
    for j in range(len(cards)):
        cards[j] = cards[j].split("_")[0]

    for j in range(len(cards)):
        try:
            cards[j] = int(cards[j])
        except:
            if cards[j] == "ACE": cards[j] = 11
            else: cards[j] = 10
    
    cards.sort()

    total = 0
    for num in cards:
        if num == 11:
            if total + 11 > 21: total += 1
            else: total += 11
        else: total += num

    return total

for i in range(cases):
    playerCards = input().rstrip().split(" ")
    dealerCards = input().rstrip().split(" ")

    playerTotal = calculateTotal(playerCards)
    dealerTotal = calculateTotal(dealerCards)

    playerBusts = playerTotal > 21
    dealerBusts = dealerTotal > 21

    message = "Tie!"
    if playerTotal > dealerTotal: message = "Player Wins!"
    elif dealerTotal > playerTotal: message = "Dealer Wins!"

    if dealerBusts: message = "Player Wins!"
    elif playerBusts: message = "Dealer Wins!"

    if dealerBusts and playerBusts: message = "Tie!"
    
    print(f"Player Score: {playerTotal} Dealer Score: {dealerTotal} {message}")