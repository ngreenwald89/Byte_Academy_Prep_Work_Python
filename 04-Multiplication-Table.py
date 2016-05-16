def print_table(x):
    sublist=[]
    listoflists=[]
    for j in range(1, x + 1):
        sublist = []
        for i in range(1, x + 1):
            k = i*j
            sublist.append(k)
        listoflists.append(sublist)
    for i in listoflists:
        head = str(i[0])
        print(head + ': ' + ' |'.join(map(str, i)))
    return listoflists
