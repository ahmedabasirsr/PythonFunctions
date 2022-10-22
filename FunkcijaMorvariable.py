# function has first and more parmeters like tuple
'''
def morvartuple(arg,*vartuple):
    print(arg)
    print("---------------")
    print(vartuple)
    return

morvartuple(20,50,40,90,100)

#we can slect any name arguments for first or tuple
def morvartuple(more,*morevaribles):
    print(more)
    print("---------------")
    print(morevaribles)
    return
morvartuple(10,20,30,55,100,99)

def morvartuple(arg,*vartuple):
    print(arg)
    print("---------------")
    for var in vartuple :
        print(var)
    return

morvartuple(10,20,30,55,100,99)
'''
def morvartuple(arg,*vartuple):
    print(arg)
    print("---------------")
    zbir=arg
    for var in vartuple :
        zbir=zbir+var
    print(zbir)
    return

morvartuple(10,20,30,55,100,99,22,5000,400)



