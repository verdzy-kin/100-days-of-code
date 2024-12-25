def Ceaser(Starttext, Shiftamnt, Cipherdirection):
    Endtext = ""
    for letter in Starttext:
        position = Alphabet.index(letter)
        if Cipherdirection == "encode":
            Shiftamnt *= -1
            Newposition = position + Shiftamnt
            Endtext += alphabet[Newposition]
            print(f"the {Cipherdirection}d text is {Endtext}")