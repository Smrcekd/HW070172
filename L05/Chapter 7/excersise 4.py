#Examscore_to_grade_convertor.py
#by David Smrček


def main():
    credit = int(input("How many credits did you get: "))

    if credit < 7 :
        print("Freshman")
    elif 6< credit <16:
        print("Junior")
    elif 16 <= credit <26:
        print("Junior")
    elif 26 <= grade:
        print("Senior")
  
        
main()
