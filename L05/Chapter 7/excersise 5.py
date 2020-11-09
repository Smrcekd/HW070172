#BMI-meassurer.py

def main():
    weight = int(input("Write your weight in pounds: "))
    height = int(input("Write your height in inches: "))
    
    BMI = (weight * 720) / height**2

    

    if BMI < 19:
        print("You are really thin")

    elif 19>= BMI <=25:
        print("Super healthy")

    elif BMI > 25:
        print("Really fat")

main()
    
