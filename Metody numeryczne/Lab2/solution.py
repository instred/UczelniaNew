
def read(path):
    with open(path, 'r') as f:
        text = f.read()
        lines = text.split('\n')
    return lines

# check palindrome count
def count_palindrome(lines):
    p_number = 0
    i = 0
    while i < len(lines):
        l, p = 0, len(lines[i]) - 1
        is_p = True
        while l < p:
            if lines[i][l] != lines[i][p]:
                is_p = False
                break
            else:
                l += 1
                p -= 1
        if is_p:
            p_number += 1
        i += 1
    return p_number

# check anagrame count
def count_anagrame(lines):
    a_number = 0
    for i in range(len(lines)):
        is_a = True
        character_count = [0] * 26
        pair = lines[i].split(" ")
        if len(pair[0]) != len(pair[1]):
            continue
        for j in range(len(pair[0])):
            character_count[ord(pair[0][j]) - 65] += 1
        for j in range(len(pair[1])):
            character_count[ord(pair[1][j]) - 65] -= 1

        for j in range(len(character_count)):
            if character_count[j] != 0:
                is_a = False
        if is_a:
            a_number += 1
    return a_number

def mirror_string(text):
    i = len(text) - 1
    out = ""
    while i > -1:
        out += text[i]
        i -= 1

    return out

def easy_caesar(text, shift):
    out = ""
    i = 0
    while i < len(text):
        out += chr( ord( text[i] ) + shift )
        i += 1
    return out

def c_encode(text, shift):
    return easy_caesar(text, shift)

def c_decode(text, shift):
    return easy_caesar(text, -shift)


def is_substring_brute(text, substr):
    if len(substr) > len(text):
        return False
    i = 0
    while i < len(text)-len(substr) + 1:
        if text[i] == substr[0]:
            j = 1
            while j < len(substr):
                if text[i+j] != substr[j]:
                    break
                j += 1
            if j == len(substr):
                return True
        i += 1
    return False

def longest_palindrome(text):
    n = len(text)
    for i in range(n-2):
        for j in range(i+1):
            flag = True
            left = j
            right = j + n - i - 1
            while left < right:
                if text[left] != text[right]:
                    flag = False
                    break
                left += 1
                right -= 1
            if flag:
                return substring(text, j, j + n - i - 1)
    return None

def substring(text, left, right):
    out = ""
    for i in range(left, right+1):
        out += text[i]

    return out


def bayer_moore(text, substr):
    n = len(text)
    m = len(substr)

    substr_alphabet = [-1] * 128
    for k in range(len(substr)):
        substr_alphabet[ord(substr[k])] = k

    start = 0
    while start <= (n-m):
        j = m-1

        while substr[j] == text[start+j]:
            j -= 1
            if j < 0:
                return True
        if j < substr_alphabet[ord(text[start+j])]:
            start += 1
        else:
            start += j - substr_alphabet[ord(text[start+j])]

    return False

def dec2any(number, system):
    out = ""
    stack = []
    while number > 0:
        stack.append(str(number % system))
        number //= system

    while stack:
        number = int(stack.pop())
        if number > 9:
            out += chr(number + 55)
        else:
            out += str(number)
    return out


def any2dec(number, system):
    i = len(number)-1
    pows = 0
    out = 0
    while i > -1:
        char = number[i]
        if not isNumber(char):
            if isUpper(char):
                out += int(ord(char) - 55) * (system**pows)
            else:
                out += int(ord(char) - 87) * (system**pows)
        else:
            out += int(char) * (system ** pows)
        i -= 1
        pows += 1

    return out

def isNumber(char):
    return not (isLower(char) or isUpper(char))

def isLower(char):
    return (ord(char) <= 122 and ord(char) >= 97)

def isUpper(char):
    return (ord(char) >= 65 and ord(char) <=90)

lines_palindromes = read("palindromy.txt")
lines_anagrames = read("anagramy.txt")
s1 = "ala ma kota"
s2 = "BABABAAAAAB"
s3 = "AAB"
s4 = "CABCBAB"
s5 = "zasdfgljdfgjyxcvbnmABCBAqweeztrtzuioio"
s6 = "AABCAAAAB"
s7 = "AAAB"

print(count_palindrome(lines_palindromes))
print(count_anagrame(lines_anagrames))
print(x := mirror_string(s1))
print(mirror_string(x))
print(x := c_encode(s1, 1))
print(c_decode(x, 1))
print(is_substring_brute(s2, s3))
print(longest_palindrome(s4))
print(bayer_moore(s6, s7))
print(dec2any(14453212, 11))
print(any2dec("EGHB2O", 25))


