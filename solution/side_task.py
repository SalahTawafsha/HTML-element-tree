""" model that encrypts a string using a key and a simple algorithm """

# The simple algorithm is to add 2 * key char value to original char

key: str = input("Enter your key: ")
original: str = input("Enter your original text: ")
encrypted: str = ""
for i, char in enumerate(original):
    encrypted += chr(ord(char) + ord(key[i % len(key)]) * 2)

print(encrypted)
