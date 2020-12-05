l = [0]*201
l[1] = 1
 
def myfunc(n):
    if n == 0 or n == 1:
        return n
    if l[n] == 0:
        l[n] = myfunc(n - 1)+ myfunc(n - 2)
    return l[n]

def myfunc_a(n):
    if n == 1:
        return n
    return myfunc(n)
 
n = int(input())
r = myfunc_a(n)
print(r%10009)