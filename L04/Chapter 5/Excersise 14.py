#WordCount.py
#Program analyzes the file to determine the number of lines, words, and characters.
#by David Smrček

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    words = []
    let = 0
    for string in data.split():
        x = string[0]
        words.append(x)
        let = len(string) + let
        average = let / (len(words))
    infile.close()

    infile = open(fname, "r")
    fileLines = infile.readlines()

    lines = []
    for line in fileLines:
        lines.append(line)
    print("There are {0} lines in the file.".format(len(lines)))
    print("The average word length is {0}".format(average))
    print("The total number of letters is {0}".format(let))
    print("The number of words is {0}".format(len(words)))
    infile.close()
main()
