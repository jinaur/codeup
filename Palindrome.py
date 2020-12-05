a = int(input())

def my_func(i, s) :
    return s[:i] + s[i+1:]

def my_func2(s) :
    n = int(len(s)/2)
    l = len(s)

    for i in range(0, n) :
        if s[i] != s[l-1-i] :
            return False
        
    return True

for i in range(0, a) :
    answer = 2
    s = input()
    r = my_func2(s)
    if r == True :
        answer = 0
    else :
        for j in range(0, len(s)) :
            s2 = my_func(j, s)
            r = my_func2(s2)
            if r == True :
                answer = 1
                break

    print(answer)