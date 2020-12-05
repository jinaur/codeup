n, k = map(int, input().split())

def Base_conversion(n, k) :
    if k == 0 :
        return 1

    elif n == -1 :
        if k % 2 == 0 :
            return 1
        else :
            return -1

    elif n == 1 :
        return 1

    else :
        return n * Base_conversion(n, k-1)





r = Base_conversion(n, k) 
print(r)