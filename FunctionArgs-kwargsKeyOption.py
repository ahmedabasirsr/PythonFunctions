def sum_Keyword(a, b, *args, option=True):
    # *args-**kwargs: * is unpacking for tuple(args)
    # **kwargs : ** is unpacking for dictionary (**kwargs)
    # option is must  = True to work this function
    ss = 0
    if option:
        for i in args:
            ss += i
        return a + b + ss
    else:
        return ss

print (sum_Keyword(1,2)) # here sum =3 only first argument(a and b)
print (sum_Keyword(1,2,3,4,5))  # here sum = 15 argument(a, b and *args)
print (sum_Keyword(1,2,3,4,5, option=False))
