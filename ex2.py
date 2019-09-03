v1=float(input("Enter relativistic speed: "))
x1=float(input("Enter light years away: "))
t1=x1/v1
t=t1/((1-v1)**(0.5))
print("It takes ",t,"light years")
