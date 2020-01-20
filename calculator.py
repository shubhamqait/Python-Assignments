my_list = []
def run_calculator():
    i = int(input("Press '1' For use calculator again else press '0' for Exit ->"))
    if bool(i):
        run_again()
    else:
        exit()


def add():
    a = 0
    for i in my_list:
        a = a + i
    print("\n\n")
    print("Ans= "+str(a))
    print("\n\n")

def enter(func):
    def wrap():
        try: 
            print("\n")
            print("Note: You Enter Unlimited Numbers But After entering all numbers type 'stop' for result")
            print("Enter first number")
            while True: 
                my_list.append(int(input())) 
                print("Enter another number")
            
        except: 
            pass

        func()   
    return wrap 


def run_again():
    while True:
        print("Press 1 for Addition")
        print("Press 2 for Substration")
        print("Press 3 for Multiplication")
        print("Press 4 for Division")
        print("Press 5 for Exit")
        i = int(input("Enter your Choice"))
        if i == 1: 
            sum = enter(add)
            sum()
            run_calculator()
        elif i == 2:
            a = float(input("\nEnter First First\n"))
            b = float(input("\nEnter another Number\n"))
            c = a-b
            print("\n\n")
            print("Ans= "+str(c))
            print("\n\n")
            run_calculator()
        elif i == 3:
            a = float(input("\nEnter First Number\n"))
            b = float(input("\nEnter another Number\n"))
            c = a*b
            print("\n\n")
            print("Ans= "+str(c))
            print("\n\n")
            run_calculator()
        elif i == 4:
            a = float(input("\nEnter Dividend\n"))
            b = float(input("\nEnter Divisor\n"))
            c = a/b
            print("\n\n")
            print("Ans= "+str(c))
            print("\n\n")
            run_calculator()
        elif i == 5:
            exit()
        else:
            print("\n\n")
            print("You Enter Wrong Choice")
            print("\n\n")

run_again()
