print("\nCalculating Students grade")

def calcgrade():
    grade_inp=int(input("Enter the grade points:"))

    if grade_inp==10:
        print("\nYour grade is O= Outstanding")
    elif grade_inp==9:
        print("\nYour grade is A+= Excellent")
    elif grade_inp==8:
        print("\nYour grade is A= Very good")
    elif grade_inp==7:
        print("\nYour grade is B= Good")
    elif grade_inp==6:
        print("\nYour grade is C= Need improvement")
    elif grade_inp<=5 and grade_inp>-1:
        print("\nYour grade is E= You are fail")
    elif grade_inp<0:
        print("\nEnter the grade from 1 to 10")
        calcgrade()
    else:
        print("\nEnter the valid code")
        calcgrade()
calcgrade()
print("\nCalculation completed")
