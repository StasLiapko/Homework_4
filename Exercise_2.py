x = list(map(int, str(input("Input number"))))
b = x[:len(x)//2]
c = list(reversed(x[(len(x)//2):]))
if b == c:
    print("Number is a palindrome")
else:
    print("Try again")