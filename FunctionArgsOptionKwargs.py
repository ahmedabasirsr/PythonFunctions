# *args-**kwargs: * is unpacking for tuple(args)
# **kwargs : ** is unpacking for dictionary (**kwargs)
# option =True : defult is true if somting is true then work somting else somting
# sequence arguments are necssery in metod(main arguments,*args,option,**kwargs)
'''
def print_args(x,y,*args,option=True,**kwargs):
    print("print main arguments as values: ",x,y)
    print("print args argument as tuple: ",args)
    print("print option ",option)
    print("print kwargs argument as dictionary: ",kwargs)


print_args(1,2,"args1","args2",a="Ahmed",b="Ali",c="Husain",d="Abas")
'''
'''
def print_args(x,y,*args,option=True,**kwargs):
    print("print main arguments as values: ",x,y)
    print("print args argument as tuple: ",args)
    print("print option ",option)
    print("print kwargs argument as dictionary: ",kwargs.items())# print tuple-list as pair


print_args(1,2,"args1","args2",a="Ahmed",b="Ali",c="Husain",d="Abas")
'''
'''
def print_args(x,y,*args,option=True,**kwargs):
    print("print main arguments as values: ",x,y)
    print("print args argument as tuple: ",args)
    print("print option ",option)
    print("print kwargs argument as dictionary: ",kwargs.values())# printonly vlues of dict.


print_args(1,2,"args1","args2",a="Ahmed",b="Ali",c="Husain",d="Abas")
'''

def print_args(x,y,*args,option=True,**kwargs):
    # function has 2 arguments(x,y), *args has 1 tuple(more values),option=True and
    # **kwargs has dictionary
    print("print main arguments as values: ",x,y)
    print("print args argument as tuple: ",args)
    print("print option ",option)
    print("print kwargs argument as dictionary: ",kwargs.values())# printonly vlues of dict.


print_args(1,2,"args1","args2",option=False ,a="Ahmed",b="Ali",c="Husain",d="Abas")
























