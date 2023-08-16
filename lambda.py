def  myfunc(n):
    return  lambda a:  a * n

mytripler = myfunc(3)

print(mytripler(33))

payl = lambda a: a * 2


james = lambda b: b * payl(20)

print(payl(10))
print(james(30))