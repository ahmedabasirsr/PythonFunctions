'''
def ifcond(x,y,z):
    if x>y and x>z :
        print (" x is great of y and z ")
    elif y>x and y>z :
        print (" y is great of x and z ")
    elif z>x and z>y :
        print (" z is great of x and y ")
    else:
        print (" is not great any value")
 
def ifcond(x,y,z):
    if  all([x >y,x >z]):
        print (" x is great of y and z ")
    elif  all([y >x,y >z]):
        print (" y is great of x and z ")
    elif all([z > x,z > y]):
        print (" z is great of x and y ")
    else:
        print (" is not great any value")
        
'''
def ifcond(x,y,z):
    if  any([x >y,x >z]):
        print (" x is great of y and z ")
    elif  any ([y >x,y >z]):
        print (" y is great of x and z ")
    elif any([z > x,z > y]):
        print (" z is great of x and y ")
    else:
        print (" is not great any value")
        
ifcond(8,5,7)
