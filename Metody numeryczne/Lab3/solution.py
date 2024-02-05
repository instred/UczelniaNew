
def compress(text):
    i = 1
    counter = 1
    out = ""
    prev = text[0]
    n = len(text)
    while i < n:
        curr = text[i]
        if curr != prev:
            out += str(counter) + prev
            counter = 1
            prev = curr
        else:
            counter += 1
            prev = curr
        if i == n-1:
            out += str(counter) + curr
        i += 1
    return out

def dec2bin(number : int):
    stack = []
    while number > 0:
        rest = number % 2
        number //= 2
        stack.append(rest)
    out = ""
    while stack:
        out += str(stack.pop())
    return out

def text2bin(text):
    i = 0
    out = ""
    while i < len(text):
        out += dec2bin(ord(text[i]))
        i += 1
    return out

def isUpper(char):
    return ord(char) >= 65 and ord(char) <= 90

def isLower(char):
    return ord(char) >= 97 and ord(char) <= 122

def isAlpha(char):
    return isLower(char) or isUpper(char)

def shift_letter(char, shift):
    if isUpper(char):
        return chr( (ord(char) + shift + 26 - 65) % 26 + 65 )
    else:
        return chr( (ord(char) + shift + 26 - 97) % 26 + 97 )


def ceasar_encode(text, shift):
    out = ""
    for i in range(len(text)):
        out += shift_letter(text[i], shift)
    return out

def ceasar_decode(text, shift):
    out = ""
    for i in range(len(text)):
        out += shift_letter(text[i], -shift)
    return out

def key_encode(text, key):
    out = ""
    i = 0
    j = 0
    while i < len(text):
        if text[i] == " ":
            out += " "
        else:
            out += shift_letter(text[i], ord(key[j]))

        i += 1
        j += 1
        j %= len(key)
    return out

def dec2bin8bit(number : int):
    stack = []
    while number > 0:
        rest = number % 2
        number //= 2
        stack.append(rest)
    out = ""
    while len(stack) < 8:
        stack.append(0)
    while stack:
        out += str(stack.pop())
    return out

def text2bin8bit(text):
    i = 0
    out = ""
    while i < len(text):
        out += dec2bin8bit(ord(text[i]))
        i += 1
    return out

def count_series(text):
    count = 1
    prev = text[0]
    i = 1
    out = ""
    while i < len(text):
        curr = text[i]
        if curr != prev:
            out += str(count) + " "
            count = 1
            prev = curr
        else:
            count += 1
        if i == len(text) - 1:
            out += str(count)
        i += 1
    return out

def fix_series(text):
    i = 0
    number = ""
    final_series = ""
    while i < len(text):
        print(i)
        while text[i] != " ":
            number+=text[i]
            i+=1
        if int(number) > 255:
            div = int(number) // 255
            r = int(number) % 255
            if r != 0:
                final_series += div * "255 0 "
                final_series += str(r) + " "
            else:
                final_series += (div-1) * "255 0 " + "255 "
        else:
            final_series += number + " "    
        number = ""
        i += 1    
        
    return final_series

def count_bits(number):
    bits = 0
    while number > 0:
        number //= 2
        bits += 1
    return bits

if __name__ == "__main__":
    s = "AAABBBBAAA"
    s2 = "!AB*"
    s3 = "WARSZAWA"
    s4 = "ALA MA KOTA"
    s5 = "PIES"
    series = "510 20 10 700 25 "
    number = 110
    shift = -2
    print(compress(s))
    print(text2bin(s2))
    print( x:= ceasar_encode(s3, shift))
    print(ceasar_decode(x, shift))
    print(key_encode(s4, s5))
    print(txt := text2bin8bit(s2))
    print(count_series(txt))
    print(fix_series(series))
    print(count_bits(700))