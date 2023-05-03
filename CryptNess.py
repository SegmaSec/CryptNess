import string
from colorit import *
init_colorit()
from six.moves import input

#DESIGN MY TOOLS
#Colors code
ORANGE=255, 165, 0
GREEN=0, 255, 0
RED=255,0,0
PINK=255,6,223
YELLOW=255, 255, 0
PURPLE=148,0,211
DEEPPINK=255,20,147
CYAN=0,238,238
WHITE=255, 255, 255

print(color("""
              ╔═╗┬─┐┬ ┬┌─┐┌┬┐╔╗╔┌─┐┌─┐┌─┐
              ║  ├┬┘└┬┘├─┘ │ ║║║├┤ └─┐└─┐
              ╚═╝┴└─ ┴ ┴   ┴ ╝╚╝└─┘└─┘└─┘""",(GREEN)) + color("\n\t\t\t\tby: Its-Sn1p3r\n\n",(WHITE)))
print(color("    --------------------------------------------------------------------------------------------------",(GREEN)))
print(color("    [$ >",(GREEN)) + color(" CryptNess is a simple Python tool for encrypting and decrypting text using the Caesar Cipher.",(WHITE))+color("|",(GREEN)))
print(color("    [$ >",(GREEN)) + color(" https://github.com/Its-Sn1p3r",(WHITE))+color("                                                                |",(GREEN)))
print(color("    [$ >",(GREEN)) + color(" https://youtu.be/b3lMKgqMOTA",(WHITE))+color("                                                                 |",(GREEN)))
print(color("    [$ >",(GREEN)) + color(" https://discord.gg/YpTYEgauM9",(WHITE))+color("                                                                |",(GREEN)))
print(color("    --------------------------------------------------------------------------------------------------\n",(GREEN)))


print("  1: "+color("Monoalphabetic Cipher \n",(ORANGE))+"  2: "+color("Transposition Cipher",(ORANGE)))
print("  3: "+color("Caesar Cipher \n",(ORANGE))+"  4: "+color("Vigenere Cipher",(ORANGE)))

menu = input("Choose Method for Cryptography: ")
print("")

#MONOALPHABETIC CIPHER
if menu == '1':
    # Choice
    print("  1) -"+color(" Encrypt \n",(CYAN))+"  2) - "+color("Decrypt",(CYAN)))
    x = int(input("Enter what do you need: "))
    print("")
    # Define the encryption key
    print(color("     Note > Plaintext/Ciphertext is Lower",(GREEN)))
    encryption_key = input(color("  Enter your Key 'lower alpha': ",(PINK)))
    plaintext = input(color("  Enter your Plaintext: ",(PINK)))

    # Define the alphabets
    lowercase_alphabet = string.ascii_lowercase
    uppercase_alphabet = string.ascii_uppercase

    # Condition
    if x == 1:
        try:
            # Define the encrypt function
            def encrypt(plaintext):
                ciphertext = ''
                for char in plaintext:
                    if char in lowercase_alphabet:
                        index = lowercase_alphabet.index(char)
                        ciphertext += encryption_key[index]
                    elif char in uppercase_alphabet:
                        index = uppercase_alphabet.index(char)
                        ciphertext += encryption_key[index].upper()
                    else:
                        ciphertext += char
                return ciphertext
            ciphertext = encrypt(plaintext)
            print(color("  >",(WHITE))+color(' Ciphertext:',(PINK)),color(ciphertext,(GREEN)))
        except:
            print("An error occurred during encryption!")

    elif x == 2:
        try:
            # Define the decrypt function
            def decrypt(plaintext):
                decrypted_text = ''
                for char in plaintext:
                    if char in lowercase_alphabet:
                        index = encryption_key.index(char)
                        decrypted_text += lowercase_alphabet[index]
                    elif char in uppercase_alphabet:
                        index = encryption_key.index(char.lower())
                        decrypted_text += uppercase_alphabet[index]
                    else:
                        decrypted_text += char
                return decrypted_text
            decrypted_text = decrypt(plaintext)
            print(color("  >",(WHITE))+color(' Decrypted text:',(PINK)),color(decrypted_text,(GREEN)))
        except:
            print("An error occurred during decryption!")
    else:
        print("Invalid choice! Please choose 1 for encryption or 2 for decryption.")


#TRANSPOSITION CIPHER
elif menu == '2':

    print("  1) -"+color(" Encrypt \n",(CYAN))+"  2) - "+color("Decrypt",(CYAN)))
    x = int(input("Enter what do you need: "))

    if x == 1:
        plaintext = input(color("  Enter your Plaintext: ",(PINK)))
        key = int(input(color("  Enter key Number: ",(PINK))))
        ciphertext = [''] * key
        for column in range(key):
            pointer = column
            while pointer < len(plaintext):
                ciphertext[column] += plaintext[pointer]
                pointer += key
        #print(''.join(ciphertext))
        print(color("  >",(WHITE))+color(" The Ciphertext is: ",(PINK))+color(''.join(ciphertext),(YELLOW)))
    elif x == 2:
        ciphertext = input(color("  Enter your Ciphertext: ",(PINK)))
        key = int(input(color("  Enter your key: ",(PINK))))
        # Determine the number of rows needed to decrypt the message
        num_rows = (len(ciphertext) // key) + (len(ciphertext) % key > 0)
        # Create a 2D list to hold the rows of the plaintext
        plaintext_matrix = [[''] * key for i in range(num_rows)]
        # Fill in the rows of the plaintext matrix with the ciphertext
        for i, c in enumerate(ciphertext):
            row = i % num_rows
            col = i // num_rows
            plaintext_matrix[row][col] = c
        # Extract the plaintext from the matrix row by row
        plaintext = ''
        for row in plaintext_matrix:
            plaintext += ''.join(row)
        print(color("  >",(WHITE))+color(" The plaintext is: ",(PINK)),color(plaintext,(YELLOW)))

#CAESAR CIPHER:
elif menu == '3':


    print("  1) -"+color(" Encrypt \n",(CYAN))+"  2) - "+color("Decrypt",(CYAN)))
    x = int(input("Enter what do you need: "))

    if x == 1:
        def caesar_cipher(plaintext, shift):
            ciphertext = ""
            for char in plaintext:
                if char.isupper():
                    # Convert uppercase letter to corresponding encrypted letter
                    ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
                elif char.islower():
                    # Convert lowercase letter to corresponding encrypted letter
                    ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    # Non-alphabetic characters are unchanged
                    ciphertext += char
            return ciphertext
        # Example usage
        plaintext = input(color("  Enter Your Plaintext': ",(PINK)))
        shift = int(input(color("  Enter Key Number: ",(PINK))))
        ciphertext = caesar_cipher(plaintext, shift)
        print(color("  >",(WHITE))+color(" The Ciphertext is: ",(PINK))+color(ciphertext,(YELLOW)))
    elif x == 2:
        ciphertext = input(color("  Enter Your Ciphertext 'Upper alpha': ",(PINK)))
        shift = int(input(color("  Enter Key Number: ",(PINK))))
        def caesar_cipher_decrypt(ciphertext, shift):
            """
            Decrypts ciphertext using Caesar Cipher with a given shift.
            """
            plaintext = ""
            for char in ciphertext:
                if char.isalpha():
                    # Shift the character by the given amount (in reverse)
                    shifted = (ord(char) - 65 - shift) % 26 + 65
                    plaintext += chr(shifted)
                else:
                    plaintext += char
            return plaintext
        plaintext = caesar_cipher_decrypt(ciphertext, shift)
        print(color("  >",(WHITE))+color(" The Ciphertext is: ",(PINK))+color(plaintext,(YELLOW)))

elif menu == '4':

    print("  1) -"+color(" Encrypt \n",(CYAN))+"  2) - "+color("Decrypt",(CYAN)))
    x = int(input("Enter what do you need: "))

    if x == 1:
        print(color("     Note > Plaintext & Key is All Upper OR Lower",(GREEN)))
        plaintext = input(color("  Enter Your Plaintext: ",(PINK)))
        key = input(color("  Enter Your Key: ",(PINK)))
        def encrypt_vigenere(plaintext, key):
            """
            Encrypts plaintext using the Vigenere Cipher with the given key.
            Preserves case of input/output.
            """
            ciphertext = ""
            key_index = 0
            for c in plaintext:
                if c.isalpha():
                    if c.isupper():
                        offset = ord('A')
                    else:
                        offset = ord('a')
                    key_char = key[key_index % len(key)]
                    key_index += 1
                    key_val = ord(key_char) - offset
                    c_val = ord(c) - offset
                    enc_val = (c_val + key_val) % 26
                    ciphertext += chr(enc_val + offset)
                else:
                    ciphertext += c
            return ciphertext
        ciphertext = encrypt_vigenere(plaintext, key)
        print(color("  >",(WHITE))+color(" The Ciphertext is: ",(PINK))+color(ciphertext,(YELLOW)))

    elif x == 2:
        print(color("     Note > Ciphertext & Key is All Upper OR Lower",(GREEN)))
        ciphertext = input(color("  Enter Your Plaintext: ",(PINK)))
        key = input(color("  Enter Your Key: ",(PINK)))
        def decrypt_vigenere(ciphertext, key):
            key_str = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
            ciphertext_codes = [ord(c) for c in ciphertext]
            key_codes = [ord(c) for c in key_str]  
            plaintext_codes = []
            for i in range(len(ciphertext_codes)):
                if ciphertext[i].isupper():
                    base = ord('A')
                elif ciphertext[i].islower():
                    base = ord('a')
                else:
                    plaintext_codes.append(ciphertext_codes[i])
                    continue
                plaintext_code = (ciphertext_codes[i] - key_codes[i] + 26) % 26 + base
                plaintext_codes.append(plaintext_code)
            plaintext = ''.join([chr(code) for code in plaintext_codes])
            return plaintext
        plaintext = decrypt_vigenere(ciphertext, key)
        print(color("  >",(WHITE))+color(" The Ciphertext is: ",(PINK))+color(plaintext,(YELLOW)))