def playfair(string, key, encrpyted):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_key = ""

    for letter in key:
        if letter not in final_key:
            final_key += letter

    letters = final_key
    string = string.replace(" ", "")
    if len(string) % 2 != 0: string += "x"

    strng = ""

    for i in range(len(string)):
        if i % 2 == 0: strng += " "
        strng += string[i]
    
    pairs = strng.strip().lower().split(" ")

    table = [ [""]*5 for i in range(5) ]
    h = len(table)
    w = len(table[0])

    shift = int(encrpyted == True) 
    for k in range(len(final_key)):
        i = int(k/w)
        j = k % h
        table[i][j] = final_key[k]

    for letter in alphabet:
        if letter not in final_key:
            k = len(letters)
            i = int(k/w)
            j = k % h
            if i < w:
                if (letter != 'j'):
                    table[i][j] = letter
                    letters += letter
        else:
            continue

    returned = ""

    for i in range(len(pairs)):
        letter = pairs[i]

        while True:
            try:
                k0 = letters.index(letter[0])
                pos0 = (int(k0/w), k0%w)

                k1 = letters.index(letter[1])
                pos1 = (int(k1/w), k1%w)

                # if same column
                if (pos0[1] == pos1[1]):
                    i0 = (pos0[0]-1 + 2*shift) % w
                    i1 = (pos1[0]-1 + 2*shift) % w
                    if(i0 < 0): i0 = w-1
                    if(i1 < 0): i1 = w-1
                    returned += table[i0][pos0[1]]
                    returned += table[i1][pos1[1]]
                # if same row
                elif (pos0[0] == pos1[0]):
                    i0 = (pos0[1]-1 + 2*shift) % h
                    i1 = (pos1[1]-1 + 2*shift) % h
                    if(i0 < 0): i0 = h-1
                    if(i1 < 0): i1 = h-1
                    returned += table[pos0[0]][i0]
                    returned += table[pos1[0]][i1]
                # if not in same column or row
                else:
                    returned += table[pos0[0]][pos1[1]]
                    returned += table[pos1[0]][pos0[1]]
                break
            except:
                if letter[0] == 'j': letter = 'i' + letter[1]
                if letter[1] == 'j': letter = letter[0] + 'i'
                continue
            
        # returned += " "

    return returned.strip()

num_keys = int(input(""))
keys = [""] * num_keys
messages = [""] * num_keys

for i in range(num_keys):
    message = input("").rstrip()
    message = message.split(" ")

    num_inputs = int(message[0])
    messages[i] = [""] * num_inputs
    keys[i] = message[1]

    for j in range(num_inputs):
        messages[i][j] = input("").rstrip()


for i in range(len(messages)):
    for j in range(len(messages[i])):
        print(playfair(messages[i][j].lower(), keys[i].lower(), False))
