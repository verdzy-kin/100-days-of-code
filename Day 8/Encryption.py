def Encrypt(Plaintext, Shiftamnt):
    Ciphertext = ""
    for letter in Plaintext:
        position = Alphabet.index(letter)
        Newposition = position + Shiftamnt
        Newletter = Alphabet[Newposition]
        Ciphertext = Ciphertext + Newletter
    print(f"the encoded text is {Ciphertext}")

def Decrypt(Ciphertext, Shiftamnt):
    Plaintext = ""
    for letter in Ciphertext:
        position = Alphabet.index(letter)
        Newposition = position - Shiftamnt
        Plaintext += Alphabet[Newposition]
    print(f"the decoded text is {Plaintext}")
def Ceaser(Starttext, Shiftamnt, Cipherdirection):
    Endtext = ""
    if Cipherdirection == "decode":
            Shiftamnt *= -1
    for char in Starttext:
        if char in Alphabet:                     
            position = Alphabet.index(char) 
            Newposition = position + Shiftamnt
            Endtext += Alphabet[Newposition]
        else:
            Endtext += char            
    print(f"the {Cipherdirection}d text is {Endtext}")
from Art import logo
print(logo)
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Continue = True
while Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    Ceaser(Starttext=text, Shiftamnt=shift, Cipherdirection=direction)
    result = input("Type 'yes' if you wanty to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        Continue = False
        print("GOODBYE")