
def read(path):
    with open(path, 'r') as f:
        text = f.read()
        lines = text.split('\n')
    return lines

def save(path, line):
    with open(path, 'a') as f:
        f.write(line+'\n')



def check_palindrome(line):
    l,r = 0, len(line)-1
    while l < r:
        if line[l] != line[r]:
            return False
        l += 1
        r -= 1
    return True

def check_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    flags = [0 for i in range(128)]
    for char in word1:
        flags[ord(char)] += 1
    for char in word2:
        flags[ord(char)] -= 1
    # tylko wielkie litery
    for i in range(128):
        if flags[i] != 0:
            return False
    return True

def mirror_encode_decode(word):
    temp = ""
    i = len(word) - 1
    while i > -1:
        temp += word[i]
        i -= 1

    return temp

def caesar_encode(word, idx):
    i = 0
    tmp = ""
    while i < len(word):
        char = chr( ord(word[i]) + idx )
        i += 1
        tmp += char

    return tmp

def caesar_decode(word, idx):
    i = 0
    tmp = ""
    while i < len(word):
        char = chr( ord(word[i]) - idx )
        i += 1
        tmp += char

    return tmp

def brute(word, subword):
    n = len(word)
    m = len(subword)
    i = 0
    while i < n-m +1:
        j = 0
        while j < m:
            if subword[j] != word[j+i]:
                break
            j+=1
        if j == m:
            return True
        i+= 1
    return False

def longestPalindrome(word):
    pass


if __name__ == '__main__':
    palindromy = 0
    anagramy = 0
    lines = read("palindromy.txt")
    for line in lines:
        if check_palindrome(line):
            palindromy += 1
#             save("palindromy_wlasciwe.txt", line)
    print(palindromy)
    lines = read("anagramy.txt")  
    for line in lines:
        word1, word2 = line.split(" ")
        if check_anagram(word1, word2):
            anagramy += 1
    print(anagramy)

    # word = input("W: ")

    # print(word := caesar_encode(word, 1))
    # print(caesar_decode(word, 1))

    w = "CABCAB"
    print(longestPalindrome(w))