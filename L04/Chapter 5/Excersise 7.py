# Caesar_cipher.py
# Program counting Caesar cipher
#by David Smrček


def main():
    text = input("Enter the words to be encrypted: ")
    key = eval(input("Enter the encryptionkey? : "))
    caesar = ""
    for ch in text:
        caesar = caesar + (chr(ord(ch) + key))

    print("Your encoded message is {0}.".format(caesar))

main()
