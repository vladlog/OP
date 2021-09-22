q = int (input ("Enter your first member of the progression: "))
w = float (input ("Enter your denominator of geometric progression (less than 1): "))
if (w < 1) :
    sum = q/(1-w) 
    print("Result is",sum)
else:
    print ("denominator of geometric progression must be less then 1,try again...")

