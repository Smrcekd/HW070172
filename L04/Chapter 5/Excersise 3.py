#Examscore_to_grade_convertor.py
#by David Smrček


def main():
    scale = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAAA"
    grade1 = int(input("Please enter the quiz grade on a scale from 0 to 100: "))
    grade2 = scale[grade1]
    print("Your number of points ({0}) is {1}.". format(grade1, grade2))
main()
