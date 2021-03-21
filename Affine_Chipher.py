def GetTextandKey():
    print("Formula: y=ax+b, x our latter")
    while True:
        try:
            a = int(input("Enter a value:"))
            b = int(input("Enter b value:"))
            plainText = input("Enter the text: ")
            return plainText, a, b
        except ValueError:
            print("You can only enter integers for a and b values")


camelAlphabet = "ABCÇDEFGĞHİIJKLMNOÖPQRSŞTUÜVWXYZ"#also you can use this code string.ascii_lowercase for english camelAlphabet but first you have to import the string module
lowerAlphabet = "abcçdefgğhiıjklmnoöpqrsştuüvwxyz"#also you can use camelAlphabet.lower(), I didn't use because sometimes that give error for turkish alphabet
alphabets = camelAlphabet + lowerAlphabet
plainText, a, b = GetTextandKey()

encryption = lambda letter: camelAlphabet[(a*camelAlphabet.index(letter)+b)%len(camelAlphabet)] if letter in camelAlphabet else lowerAlphabet[(a*lowerAlphabet.index(letter)+b)%len(lowerAlphabet)]#Formula is y=a*x+b -> y=new letter, x=old letter
print("".join((map(lambda letter: encryption(letter) if letter in alphabets else letter, plainText))))


