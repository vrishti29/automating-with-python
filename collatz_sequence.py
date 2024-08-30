def collatz(n):
    if n%2 == 0:
        a = n//2
    
    elif n%2==1:
        a = 3*n +1
    
    else:
        print("Enter a number")

    print(a)
    return a
    
    
def sequence(n):
    while n!= 1:
        n = collatz(n)

number = 10
sequence(number)