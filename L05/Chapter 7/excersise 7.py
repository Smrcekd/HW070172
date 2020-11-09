#Babysitter.py
    
    
def main():
        time1 = input("Please write the starting (hh:mm): ")
        time2 = input("Please write the finishing time (hh:mm): ")

        startMin = eval(time1[-2:len(time1)])
        startHr = eval(time1[:len(time1)-3])
        endMin = eval(time2[-2:len(time2)])
        endHr = eval(time2[:len(time2)-3])

        time1 = startHr + 1 / (60/startMin)
        endTime = endHr + 1 / (60/endMin)
        time = time2 - time1
        
        if time2 < 21:
            bill = time * 2.50
        else:
            x = time2 - 21
            bill = (time - x) * 2.50 + (x * 1.75)
        print("Babysitter earned", bill ,"." )
main()
