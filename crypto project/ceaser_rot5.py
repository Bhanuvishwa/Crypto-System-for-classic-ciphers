import re
import sys


def cipher_encryption(rot5, zero_to_nine):
    message = input("Enter message: ")

    if not re.search('[\d\s]+', message):
        print("Entered message is not an integer")
        sys.exit()

    encryp_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            encryp_text += " "
        else:
            for j in range(len(zero_to_nine)):
                if message[i] == zero_to_nine[j]:
                    encryp_text += rot5[j]

    print("Encrypted Text: {}".format(encryp_text))


def cipher_decryption(rot5, zero_to_nine):
    message = input("Enter message: ")

    if not re.search('[\d\s]+', message):
        print("Entered message is not an integer")
        sys.exit()

    decryp_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            decryp_text += " "
        else:
            for j in range(len(zero_to_nine)):
                if message[i] == rot5[j]:
                    decryp_text += zero_to_nine[j]

    print("Decrypted Text: {}".format(decryp_text))



rot5 = "5678901234"
zero_to_nine = "0123456789"

choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
if choice == 1:
    print("---Encryption---")
    cipher_encryption(rot5, zero_to_nine)

elif choice == 2:
    print("---Decryption---")
    cipher_decryption(rot5, zero_to_nine)

else:
    print("Invalid Choice")

