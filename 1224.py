a, b, c, d = list(map(int, input().split()))

if float(a/b) > float(c/d) :
    print(">")
if float(a/b) == float(c/d) :
    print("=")
if float(a/b) < float(c/d) :
    print("<")

