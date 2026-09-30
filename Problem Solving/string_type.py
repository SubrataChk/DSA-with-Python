
# Character Frequency Count
def char_frequency(s):
    freq = {}
    for ch in s:
        count = 0
        for c in s:
            if c == ch:
                count += 1
        freq[ch] = count
    return freq


# def char_frequency(s):
#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1
    # return freq

print(char_frequency("banana"))



# Reverse a String
def reverse_string_manual(s):
    charts = list(s)
    print(s)
    left, right = 0, len(charts) - 1
    while left < right:
        charts[left], charts[right] = charts[right], charts[left]
        left += 1
        right -= 1
    return "".join(charts)


# print(reverse_string_manual("World"))

# Time: O(n). Space: O(n) (notun string/list toiri hocche, string immutable bole)




# Anagram Check
# Anagram mane duita string-er characters same, kintu order alada (jemon "listen" ar "silent").
# Approach: Duita string sort kore compare kora, othoba character frequency count kore compare kora.

def is_anagram(s: str, t: str):
    s = s.lower()
    t = t.lower()
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if  count.get(ch, 0) == 0:
            return False
        count[ch] -= 1

    return True

# print("Is Anagram -> ", is_anagram("listen", "silent"))



# Palindrome Check
# Palindrome mane hocche emon string, ja shamne theke porleo same, pichon theke porleo same (jemon "madam",
# "racecar").
# Approach: Two-pointer diye front ar back compare kora, othoba string reverse kore compare kora.

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# print(is_palindrome("Madama"))


# s = "Hello DSA world"
# print(s.lower())
# print(s.upper())
# print(s.strip())
# print(s.count("l"))
# print(s.find("DSA"))
# print(s.replace("world", "universe"))
# print(list(s))