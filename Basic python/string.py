text = "Hello world"

print(text.lower())
print(text.upper())
print(text.split())
print("-".join(text))
print(text[::-1])
print(text.replace("world", "python"))
print(len(text))

print(text[0])
#Important: Python e string immutable — mane string-er kono character direct change kora jay na. 
# Notun string banate hoy.

# s = "hello"
# # s[0] = "H" s = "H" + s[1:] # ERROR!
# # new string toiri kore -> "Hello"