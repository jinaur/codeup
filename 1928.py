n = int(input())

def my_func(n) :
    answer = n
    if answer == 1 :
        return 1
    if answer%2 == 1 :
        answer = (answer * 3) + 1
        print(answer)
        return my_func(answer)
    else :
        answer = answer // 2
        print(answer)
        return my_func(answer)
    
print(n)

r = my_func(n)