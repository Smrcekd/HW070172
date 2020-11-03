# Program counting the average word lenght.py
# In the sentence entered by the user
#by David Smrček


def main():
    text = input("Write the sentence: ")
    words = []
    for string in text.split():
        x = string[0]
        words.append(x)

    let = 0
    for string in text.split():
        let = len(string) + let
        average = let / (len(words))
    print(average)

main()
