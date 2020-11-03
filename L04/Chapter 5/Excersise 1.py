#dataconvert.py


def main():
   
    dayNr = int(input("Enter the day number: "))
    monthNr = int(input("Enter the month number: "))
    yearNr = int(input("Enter the year: "))

    date1 = str(monthNr)+"/"+str(dayNr)+"/"+str(yearNr)

    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[monthNr-1]
    date2 = monthStr+" " + str(dayNr) + ", " + str(yearNr)

    print("The date is {0} or {1}.".format(date1, date2))

main()
