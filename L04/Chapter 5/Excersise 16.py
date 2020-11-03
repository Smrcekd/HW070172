#QuizScoreHistogram.py
#I absolutely did not know how to do this, so I got a lot of help from others
#I wasnt able to make it work
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    scores = [0,0,0,0,0,0,0,0,0,0,0]
    students = 0

    for line in infile.readlines():
        scores[int(line)] = scores[int(line)]+1
        students = students + 1

    height = max(scores)

    win = GraphWin('Quiz Histogram', 640, 480)
    win.setCoords(0, 0, 35, height * 1.5)

    students = 'Total Students: '+str(students)

    totalStudent = Text(Point(8,.1 * height), students)
    totalStudent.draw(win)

    pos = 2
    hgt = .2 * height
    for i in range(11):
        bar = Rectangle(Point(pos, hgt),Point(pos + 2, scores[i] + hgt))
        bar.setFill('red')
        bar.draw(win)

        pos = pos+3

    position = 3
    hgt = .1 * height +  1
    for i in range(11):
        Text(Point(position, hgt), i).draw(win)
        position = position + 3

    win.getMouse()
    win.close()


    infile.close()

main()

