# Program counting the number of words.py
# In the sentence entered by the user
#by David Smrček


def main():
    text = input("Write the sentence: ")
    letters = []
    
    for string in text.split():
        x = string[0]
        letters.append(x)
        
    print(len(letters))

main()
