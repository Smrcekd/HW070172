#excersise1.py

def main():
    hours = int(input("How many hours have you worked? "))
    wage = int(input("How much do you earn per hour? "))

    wph = hours * wage
    

    if hours <= 40:
        final = wph
        print(final)
        

    else:
        final = 40* wage
        final = (hours - 40) * 1.5 * wage + final
        print(final)
    

main()
    
