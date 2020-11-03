# acronym_creator.py
#by David Smrček


def main():
    title = input("Enter the words for acronym: ")
    words = []
    for string in title.split():
        x = string[0].upper()
        words.append(x)
    acronym = "".join(words)
    print(acronym)

main()
