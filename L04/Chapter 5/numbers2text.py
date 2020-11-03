#text2numbers.py


def main():

    print("This program converts Unicode message into strings of text")

    inString = input("Please enter the Unicode-encoded message: ")

    message = " "
    for numStr in inString.split():
        codeNum = int(numStr)
        message = message + chr(codeNum)
    
    print("/nThe decoded message is:", message)

main()
