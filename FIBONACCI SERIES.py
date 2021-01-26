num = int(input("enter the number of terms: "))
f1,f2 = 0,1
f3=f1+f2
print("\nThe Fibonacci series of first",num,"terms")

print(f1)
print(f2)

for i in range(2,num):
    print(f3)
    f1=f2
    f2=f3
    f3=f1+f2
