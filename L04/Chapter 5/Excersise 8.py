# Caesar_cipher2.py
# Program counting upgraded Caesar cipher
#by David Smrček


def main():
    text = input("Enter the words to be encrypted: ")
    key = eval(input("Enter the encryptionkey? : "))

    text = text.lower()
    table = "abcdefghijklmnopqrstuvwxyz"
    caesar = ""
    for ch in text:
        caesar = caesar + (table[((ord(ch))-97) + key%52])

    print("Your encoded message is {0}.".format(caesar))

main()
