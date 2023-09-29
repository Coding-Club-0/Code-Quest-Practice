cases = int(input().rstrip())
anyB = [["'; ", " --"], ["${", "}"], ["$(", ")"]]
caseSensitive = ["&& sudo", "&& su -", ";;", "%s", "%x", "%n"]
caseInSensitive = ["' OR 1=1", "<script"]

for trial in range(cases):
    value = str(input().rstrip())
    invalid = False

    for case in caseSensitive:
        if case in value:
            print("REJECTED")
            invalid = True  
            break
    
    if invalid: continue

    for case in caseInSensitive:
        if case.lower() in value.lower():
            print("REJECTED")
            invalid = True
            break

    if invalid: continue

    for case in anyB:
        new_value = value

        first, second = case
        while first in new_value and second in new_value:
            firstIndex = new_value.index(first)
            secondIndex = new_value.index(second)
            if secondIndex > firstIndex:
                print("REJECTED")
                invalid = True
                break

            new_value = value[firstIndex+len(first):]

    if not invalid:
        print(value)
    

            
