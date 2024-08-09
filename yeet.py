x = 0
def auto_count(x):
    i = 0
    if x == 0:
        print("please enter and int")
        return
    else:
        for i in range(x):
            print(i)
            i =+ 1
    #print("please enter a digit greter that 0")
x = int(input("please enrtr a dget to coun to :"))
auto_count(x)