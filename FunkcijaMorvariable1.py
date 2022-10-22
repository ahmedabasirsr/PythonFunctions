def strin1(arg,*vartuple):
    # arg is 1 argument(Ahmed). *vartuple is tuple and it has more varaibles
    s = arg+" "
    for v in vartuple:
        # for loop in tuple vartuple
        s = s+" "+v
    print(s)
    return

strin1("arg = Ahmed"," *vartuple = is","a","student","student","student")
