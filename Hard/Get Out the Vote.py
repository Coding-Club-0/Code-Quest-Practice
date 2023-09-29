# cases = int(input().rstrip())
# data = [''] * cases

# def vote(arr):
#     candidates = ""
#     counts = []
#     for ballot in arr:
#         if ballot[0] not in candidates: 
#             candidates += ballot[0]
#             counts.append(1)
#         else:
#             counts[candidates.index(ballot[0])] += 1
#     return [[*candidates], counts]

# for i in range(cases):
#     ballots, candidates = list(map(int, input().rstrip().split(" ")))
    
#     people = [''] * ballots
#     for j in range(ballots):
#         people[j] = input().rstrip()
    
#     finalWinner = 0
#     finalVotes = 0
    
#     tallies = 0
#     while True:
#         winners, votes = vote(people)
#         tallies += 1
#         minValue = votes[0]
#         minIndex = 0

#         maxValue = votes[0]
#         maxIndex = 0

#         for j in range(1, candidates):
#             if votes[j] > maxValue:
#                 maxValue = votes[j]
#                 maxIndex = j

#             if votes[j] < minValue:
#                 minValue = votes[j]
#                 minIndex = j

       
#         if votes[maxIndex] / ballots > 0.5:
#             finalWinner = winners[maxIndex]
#             finalVotes = '%.1f' % round(100 * votes[maxIndex] / ballots, 1)
#             break
            
#         loser = winners[minIndex]

#         for j in range(ballots):
#             people[j] = [*people[j]]
#             try: people[j].remove(loser)
#             except: a = 0
#             people[j] = ''.join(people[j])

#         candidates -= 1
#         if candidates == 1:
#             finalWinner = winners[0]
#             finalVotes = '%.1f' % round(100 * votes[0] / ballots, 1)
#             break

#     data[i] = f'Candidate {finalWinner} won with {finalVotes}% of the vote after {tallies} tallies'

# for i in range(cases): print(data[i])

cases = int(input().rstrip())
data = [''] * cases

def vote(arr):
    candidates = ""
    counts = []
    for ballot in arr:
        if ballot[0] not in candidates: 
            candidates += ballot[0]
            counts.append(1)
        else:
            counts[candidates.index(ballot[0])] += 1
    return [[*candidates], counts]

for i in range(cases):
    try:
        ballots, candidates = list(map(int, input().rstrip().split(" ")))
    except ValueError:
        print("Error: Invalid input format. Please enter two integers separated by a space.")
        continue
    
    people = [''] * ballots
    for j in range(ballots):
        people[j] = input().rstrip()
    
    finalWinner = 0
    finalVotes = 0
    
    tallies = 0
    while True:
        try:
            winners, votes = vote(people)
        except IndexError:
            print("Error: Invalid input format. Please make sure the number of candidates matches the length of the candidate names.")
            break
        
        tallies += 1
        minValue = votes[0]
        minIndex = 0

        maxValue = votes[0]
        maxIndex = 0

        for j in range(1, candidates):
            if votes[j] > maxValue:
                maxValue = votes[j]
                maxIndex = j

            if votes[j] < minValue:
                minValue = votes[j]
                minIndex = j

       
        if votes[maxIndex] / ballots > 0.5:
            finalWinner = winners[maxIndex]
            finalVotes = '%.1f' % round(100 * votes[maxIndex] / ballots, 1)
            break
            
        loser = winners[minIndex]

        for j in range(ballots):
            people[j] = [*people[j]]
            try: people[j].remove(loser)
            except ValueError: pass
            people[j] = ''.join(people[j])

    
        candidates -= 1
        if candidates == 1:
            finalWinner = winners[0]
            finalVotes = '%.1f' % round(100 * votes[0] / ballots, 1)
            break

    data[i] = f'Candidate {finalWinner} won with {finalVotes}% of the vote after {tallies} tallies'

for i in range(cases): print(data[i])
