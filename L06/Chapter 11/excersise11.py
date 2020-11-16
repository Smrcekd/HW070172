#Censor
def main():
    fname = "list.txt"
    infile = open(fname, "r")
    outfile = open("list.txt", "w")
    for line in infile:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) == 4:
                words[i] = "****"
        line = " ".join(words)
        print((line), file = outfile)
    infile.close()
    outfile.close()
main()
