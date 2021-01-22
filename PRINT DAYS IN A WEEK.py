print("\nPrinting days in a week")

def days():
    num=int(input("\nEnter the number:"))

    if num==1:
        print("Day is Monday")
    elif num==2:
        print("Day is Tuesday")
    elif num==3:
        print("Day is Wednesday")
    elif num==4:
        print("Day is Thursday")
    elif num==5:
        print("Day is Friday")
    elif num==6:
        print("Day is Saturday")
    elif num==7 or num==0:
        print("Day is Sunday")
    else:
        print("\nEnter the correct number")
        days()
    
days()
print("\nThe process ends")
        
