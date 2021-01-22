print("\nTraffic signals")

def signal():
    num_inp=int(input(''' choose the option

1)red
2)yellow
3)green

enter the correct value:'''))

    if num_inp ==1:
        print("Stop")

    elif num_inp ==2:
        print("Get ready")

    elif num_inp ==3:
        print("Go")

    else:
        print("enter the correct value")
        signal()

signal()
print("\nThe process ends")
    
