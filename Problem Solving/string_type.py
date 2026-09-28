
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


print(is_palindrome("Madama"))


# s = "Hello DSA world"
# print(s.lower())
# print(s.upper())
# print(s.strip())
# print(s.count("l"))
# print(s.find("DSA"))
# print(s.replace("world", "universe"))
# print(list(s))