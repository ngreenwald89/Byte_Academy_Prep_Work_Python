#not sure why nested for loops requested...
def triangle(n):
    for i in range(1, 2):
        for j in range(1, n + 1):
            print('*' * i * j)

#possible with single for loop
def simple_t(n):
    for j in range(1, n + 1):
        print('*' * j)
