import argparse
parser.argparse.ArgumentParser(description="Do Something.")

#i=1
#h=float(input("Hight of the building: "))
#h=float(sys.argv[1])
g=9.8
parser.add_argument('h',type=float,help='height of the object')
t=(((2*h)/g))**(1/2)
#a=sys.argv.__sizeof__
#while (i<((int(sys.argv.count)))+1):
print (t)
im