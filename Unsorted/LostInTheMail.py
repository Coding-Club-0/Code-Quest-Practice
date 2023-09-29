cases = int(input().rstrip())

def getData(string):
    output = ""
    for j in range(len(string)):
        if string[j] == "T": output += "00"
        elif string[j] == "A": output += "01"
        elif string[j] == "D": output += "10"
        else: output += "11"
    output = int(output, 2)
    tracking = ""
    for j in range(18):
        tracking = str(output % 10) + tracking
        output //= 10
    output //= 50
    routing = output - 100001
    final = tracking + str(routing)
    
    first3 = final[0:3]
    serviceType = 0

    if first3 == "042" or first3 == "261": serviceType = 0
    elif first3 == "040" or first3 == "300": serviceType = 1
    elif first3 == "710" or first3 == "712": serviceType = 2

    mailerId = final[3:9]
    serialNo = final[9:18]

    zipCode5 = final[18:23]
    zipCode4 = final[23:]

    return [serviceType, mailerId, serialNo, zipCode5, zipCode4]

for i in range(cases):
    letters = int(input().rstrip())
    classes = [0, 0, 0]
    mailerIds = []
    mailerCounts = []
    zipCodes = []
    zipCounts = []

    for j in range(letters):
        string = input().rstrip()
        data = getData(string)
        classes[data[0]] += 1

        id = data[1]
        if id not in mailerIds: 
            mailerIds.append(id)
            mailerCounts.append(1)
        else:
            index = mailerIds.index(id)
            mailerCounts[index] += 1

        zipCode = data[3]
        if zipCode not in zipCodes: 
            zipCodes.append(zipCode)
            zipCounts.append(1)
        else:
            index = zipCodes.index(zipCode)
            zipCounts[index] += 1
        
    mostMailer = mailerIds[0]
    mostCounts = mailerCounts[0]
    for j in range(1, len(mailerIds)):
        if mailerCounts[j] > mostCounts:
            mostMailer = mailerIds[j]
            mostCounts = mailerCounts[j]

    mostZip = zipCodes[0]
    mostZipCounts = zipCounts[0]
    for j in range(1, len(zipCodes)):
        if zipCounts[j] > mostZipCounts:
            mostZip = zipCodes[j]
            mostZipCounts = zipCounts[j]

    print(f'Packages Sorted: {letters}\nStandard Class: {classes[0]}\nFirst Class: {classes[1]}\nPriority Mail: {classes[2]}\nMost frequent mailer ID: {mostMailer}\nMost frequent ZIP code: {mostZip}')
