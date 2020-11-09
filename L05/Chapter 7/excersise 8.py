#USsenatorrepresentative.py
    
    
def main():
    citizenship = eval(input("How many years have you had citizenship? "))
    age = eval(input("How old are you? "))
    if citizenship >= 9:
        if age >= 30:
            print("You can be senator or a representative.")
        elif 30 > age >= 25:
            print("You can be representative, but not a senator.")
        else:
            print("You cannot be senator nor representative.")
    else:
        print("You cannot be senator nor representative.")
main()
