r = int(input("Input radius "))
x = int(input("Input x "))
y = int(input("Input y "))
b = list(range(-r, r+1))
if abs(x) and abs(y) in b:
    print ("In range")
else: print("Error")