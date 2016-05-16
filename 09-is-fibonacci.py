def is_fib(n):
    l=[0,1]
    z=1
    i=0
    if n<0 or n!=int(n):
        return False
    elif n==0 or n==1:
        return True
    else:
        while n>=z:
            l.append(l[i]+l[i+1])
            z=l[i+2]
            if n==z:
                return True
                break
            i=i+1
        return False
