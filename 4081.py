n = int(input())

if n < 74 and n > 1:
    a = "blue"
    b = "recommend"
elif 74 <= n < 100 : 
    a = "green"
    b = "possible"
elif 100 <= n < 148	:
    a = "yellow"
    b = "careful"
elif 148 <= n and n <= 1000 :
    a = "red"
    b = "stop"

else :
    a = "data"
    b = "error"

print(n, a, b)
