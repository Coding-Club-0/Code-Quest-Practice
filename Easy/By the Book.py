cases = int(input().rstrip())
data = [0] * cases


def is_valid_isbn10(isbn):
    # Check if the length of the ISBN is 10
    if len(isbn) != 10:
        return False

    # Calculate the checksum
    checksum = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        checksum += int(isbn[i]) * (i + 1)

    # Check the last digit
    if isbn[-1] == 'X':
        checksum += 10 * 10
    elif isbn[-1].isdigit():
        checksum += int(isbn[-1]) * 10
    else:
        return False

    # Validate the checksum
    if checksum % 11 == 0:
        return True
    else:
        return False
    
for i in range(cases): data[i] = input().rstrip()
for i in range(cases):
    code = data[i]
    print(is_valid_isbn10(code))
    