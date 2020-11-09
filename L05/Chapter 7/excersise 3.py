#Examscore_to_grade_convertor.py
#by David Smrček


def main():
    grade = int(input("Please enter the quiz grade on a scale from 0 to 100: "))
    if grade > 100:
        Print("Write normal number, dude")
    elif 90 < grade <=100:
        print("A")
    elif 80< grade < 90:
        print("B")
    elif 70 < grade < 80:
        print("C")
    elif 60 < grade < 70:
        print("D")
    elif grade <60:
        print("F")
        
main()
