#HorizontalBarChart.py
#Program to plot a horizontal bar chart of student exam scores.
#I absolutely did not know how to do this, so I got a lot of help from others
#I wasnt able to make it work
from graphics import *
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    stud = int(infile.readline())
    name = []
    grade = []
    lines = []
    for line in infile.readlines():
        x, y = line.split(": ")
        y = y[0:-1]
        name.append(x)
        grade.append(y)

    print(name)
    print(grade)
    win = GraphWin("Student Grade Chart", 400, 50 * stud)
    win.setCoords(-30, (10 * stud + 2), 120, 0)
    for i in range (numStud):
        s = name[i].rjust(10)
        Text(Point(-20, 15 + stud * .8 * i), s).draw(win)
    for i in range (numStud):
        r = Rectangle(Point(0, 13 + numStud * .8 *i), Point(grade[i], 17 + numStud * .8 * i))
        r.draw(win)
    infile.close()
main()

