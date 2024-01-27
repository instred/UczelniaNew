def code_string(text):
    out = ""
    i = 1
    length = 1
    current = text[0]
    while i < len(text):
        while i < len(text) and current == text[i]:
            length += 1
            i += 1
        out += str(length)+current
        if i < len(text):
            length = 1
            current = text[i]
        i += 1
    if out[-1] != text[-1]:
        out += str(length)+text[-1]
    return out

def code_string2(text):
    out = ""
    for i in range(len(text)):
        binar = []
        num = ord(text[i])
        curr_binar = ""
        dec_to_bin(num, binar)
        for i in range(1, len(binar)):
            curr_binar += str(binar[i])
        out += curr_binar+" "
        curr_binar = ""
    return out

def dec_to_bin(num, binar):
    if num >=1:
        dec_to_bin(num//2, binar)
    binar.append(num%2)

def shift_letters(text, shift):
    new = ""
    for i in range(len(text)):
        val = text[i]
        new += shift_letter(val, shift)
    return new

def codeCaesar(text, shift):
    return shift_letters(text, shift)


def decodeCaesar(text, shift):
    return shift_letters(text, -shift)

def is_upper(letter):
    val = ord(letter)
    if val >= 65 and val <= 90:
        return True
    return False

def is_lower(letter):
    val = ord(letter)
    if val >= 97 and val <= 122:
        return True
    return False

def is_letter(letter):
    return is_lower(letter) or is_upper(letter)

def cipherKey(text, key):
    new = ""
    for i in range(len(text)):
        if text[i] != "":
            shift = ord(key[i%len(key)])
            new  += shift_letter(text[i], shift)
    return new

def shift_letter(letter, shift):
    val = letter
    if is_upper(val):
        val = chr((ord(val) + shift + 26 - 65) % 26 + 65)
    elif is_lower(val):
        val = chr((ord(val) + shift + 26 - 97) % 26 + 97)
    return val


if __name__ == "__main__":
    s = "AAAAAABBBAAABBA"
    s2 = "!AB*"
    s3 = "WARSZAWA"
    s4 = "ALA MA KOTA"
    s5 = "PIES"
    shift = -2
    print(code_string(s))
    print(code_string2(s2))
    print(codeCaesar(s3, shift))
    print(decodeCaesar(codeCaesar(s3, shift), shift))
    print(cipherKey(s4, s5))