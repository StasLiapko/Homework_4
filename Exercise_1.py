x = list(map(int, str(input("Input number"))))
b = x[:len(x)//2]
c = x[len(x)//2:]
if sum(b) == sum(c):
    print("Lucky ticket")
else:
    print("Good luck next time")