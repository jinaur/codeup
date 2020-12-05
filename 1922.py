n = int(input())

def my_func(n, count) :
    answer = n
    if answer == 1 :
        return count
    if answer%2 == 1 :
        answer = (answer * 3) + 1
        count += 1
        return my_func(answer, count)

    else :
        answer = answer // 2
        count += 1
        return my_func(answer, count)
    
count = 1
r = my_func(n, count)

print(r)