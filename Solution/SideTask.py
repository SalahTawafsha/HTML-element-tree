key: str = input("Enter your key: ")
original: str = input("Enter your original text: ")
encrypted: str = ""
for i in range(len(original)):
    encrypted += chr(ord(original[i]) + ord(key[i % len(key)]) * 2)

print(encrypted)
