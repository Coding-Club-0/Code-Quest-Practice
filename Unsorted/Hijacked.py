cases = int(input().rstrip())

def findHidden(string):
    messages = []
    i = 0
    while i < len(string):
        triplet = string[i:i+3]

        if " " in triplet: 
            continue

        if triplet[::-1] in string[i+3:]:
            message = string[i+3:string.index(triplet[::-1])]
            i += len(message)
            messages.append(message)
            continue
        
        i += 1
    return messages

def removeContiguous(message):
    i = 0
    new_message = ""
    while i < len(message):
        new_message += message[i]

        if i+1 < len(message) and message[i] == message[i+1]:    
            i += 2
            continue
        i += 1
    return new_message

for case in range(cases):
    N = int(input().rstrip())
    message = input().rstrip()
    messages = findHidden(message)
    for m in messages:
        print(removeContiguous(m))