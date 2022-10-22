
# lambda is specification funcion, it is executive in one line.
# it has more enter parmaters,: and any proceses you can to executive

zbir=lambda x,y : x+y
print(zbir(5,8))


m=lambda x,y : x*y+10
print(m(6,4))


d = lambda x,y,z : x/y-z
s =d(4,2,1)
print(s)

# function with lambda
def fun_lam(n,x,y):
    zbir=lambda x,y : x+y
    print(zbir(x,y)*n)

fun_lam(5,3,4)

