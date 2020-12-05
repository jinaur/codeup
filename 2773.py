n, k = input().split()
n = int(n)

for i in range(0, n) :
    a, b = input().split(",")
    print('"' + a + '"' + "," , end="")
    print('"' + b + '"' + "," , end="")
    print('"' + k + '"' + "," , end="")
    print('"' + "0" + '"' + "," , end="")
    print('"' + "" + '"' + "," , end="")
    print('"' + "0" + '"' + "," , end="")
    print('"' + "0" + '"')

