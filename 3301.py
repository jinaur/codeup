n = int(input())

count = 0
arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for r in arr : 
    a = n//r
    if a > 0 :     
        count += a
        n -= a * r
        

print(count)


