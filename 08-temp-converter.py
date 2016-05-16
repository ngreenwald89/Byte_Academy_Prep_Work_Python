def fahr_cel(f):
#    declare 5/9 as floats so division works properly
    c = (5.0/9.0)*(f-32)
    c = round(c,1)    
    return c

def cel_fahr(c):
#    declare 9/5 as float so division works properly
    f = (9.0/5.0)*c+32
    f = round(f,1)
    return f
