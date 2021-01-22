print("\nRoot of quadratic equation")

def quaeqn():
    A=int(input("enter the value of A:"))
    B=int(input("enter the value of B:"))
    C=int(input("enter the value of C:"))
    quad=(B**2)-(4*A*(C))

    if quad>0:
        print("There are two solutions")
    elif quad<0:
        print("It is complex solution")
    else:
        print("It has only one solution")

quaeqn()
print("\nThe process ends")
