caesar_encryption = lambda my_string, empty_string="": empty_string.join(chr(ord(my_char) + 1) for my_char in my_string)

print(caesar_encryption('a'))
print(caesar_encryption('ABC'))
print(caesar_encryption('Rock2021'))
