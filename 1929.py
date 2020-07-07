n = int(input())

def reverse(n):
    if n == 1:
        return print(n)
    elif n%2:
        reverse(3*n+1)
    else: 
        reverse(n//2)
    return print(n)

r = reverse(n)
