def mario_triangle(n):
    for i in range(1, 2):
        for j in range(n - 1, -1, -1):
            print(' ' * ( i * j) + '*' * (n - j)) 

#also works, but doesn't use nested for loops, just one for loop
def simple_mario(n):
    for j in range(n - 1, -1, -1):
        print(' ' * j + '*' * (n - j))
