a=[1,2,3,4,5,0,-1,-2,-3,-4,-5]
for i in a:
    if(i>0):
        print("positive numbers are",i)
n=int(input("enter a number:"))
sr=[i**2 for i in range(1,n+1)]
print(sr)

