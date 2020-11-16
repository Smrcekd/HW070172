# Windchill index

def windc(T, V):
    if 50 >= V >= 3:
        windc = 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) + (0.4275 * T) * (V ** 0.16)
    else:
        windc = 0
    return windc

def main():
    print("{0:>11} {1:6} {2:6} {3:6} {4:>6} {5:6} {6:6} {7:6}".format(-20, -10, 0, 10, 20, 30, 40, 50))
    print("")
    for i in range (11):
        print("{0:2} {1:>8.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".format(i*5,windchill(-20, i*5), windchill(-10, i*5), windchill(0, i*5), windchill(10, i*5), windchill(20, i*5), windchill(30, i*5), windchill(40, i*5), windchill(50, i*5)))

main()
