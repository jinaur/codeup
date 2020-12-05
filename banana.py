a, b, c = map(int, input().split())
 
n, m = map(int, input().split())
 
a_count = 0 
b_count = 0 
 
total_count = m - n + 1
 
if a < c/b :
    a_count = total_count
else:
    for i in range(n, m+1) :
        a_cost = i * a
        b_cost = i // b * c
 
        if i % b > 0 :
            b_cost += c
 
        if a_cost <= b_cost :
            a_count += 1
        else :
            b_count = total_count - a_count
            break
 
print(a_count)
print(b_count)
