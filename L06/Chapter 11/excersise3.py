#gpasort3.py

from gpa import Student, makeStudent

def makeStudents(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),file = outfile)
    outfile.close()

def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    while True:
        x = (input('Type "Gpa", "name", or "credits" to sort accoring to those categories: '))
        y = (input('Type "Ascending"or "Descending" depending on how you want your list.'))

        if x == 'GPA':
            data.sort(key=Student.gpa)
            s = "_(GPA)"
            if m == "D":
                data.reverse()
            break
        elif x == 'name':
            data.sort(key=Student.getName)
            s = "_(name)"
            if m == "D":
                data.reverse()
            break
        elif x == 'credits¨':
            data.sort(key=Student.getQpoints)
            s = "_(credits)"
            if m == "D":
                data.reverse()
            break
        else:
            print("Wrong input, write 'GPA', 'name' or 'Credits'")
            
    data.sort(key = Student.gpa)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()
