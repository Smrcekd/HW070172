#Speed limit meassurer.py

def main():
    x = int(input("What was your speed: "))
    y = int(input("Maximum speed limit: "))
    
    OTL = x - y
    
    if OTL >= 0:
        fine = (OTL // 5) * 5 + 50
        if x >= 90:
            fine = fine + 200
        print("The fine is", fine)
    elif OTL < 0:
        print("You don´t have to pay anything.")
    
main()
    
