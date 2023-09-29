cases = int(input().rstrip())
data = [0] * cases

for i in range(cases):
    game = input().rstrip().split(" ")
    rock = game.count("R")
    paper = game.count("P")
    scissors = game.count("S")
    
    winners = 0
    if rock == 1 and scissors > 0 and paper == 0:
        data[i] = "ROCK"
        winners += 1
    if scissors == 1 and paper > 0 and rock == 0:
        data[i] = "SCISSORS"
        winners += 1
    if paper == 1 and rock > 0 and scissors == 0:
        data[i] = "PAPER"
        winners += 1
    
    if winners != 1:
        data[i] = "NO WINNER"

for i in range(cases):
    print(data[i])