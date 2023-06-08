def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
#check the above function
# text = "CEASER CIPHER DEMO"
# s = 5
# print ("Plain Text : " + text)
# print ("Shift pattern : " + str(s))
# print ("Cipher: " + encrypt(text,s))


def decrypt(text):
    s = 1
    for r in range(25):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text
            
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        s += 1
        print(r , "=" , result)

text = "GIEWIVrGMTLIVrHIQS"
decrypt(text)
