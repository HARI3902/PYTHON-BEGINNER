value = 5
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print("The factorial: ",fact(value))
