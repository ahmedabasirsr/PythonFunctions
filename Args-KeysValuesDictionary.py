# *args-**kwargs: * is unpacking for tuple(args)
# **kwargs : ** is unpacking for dictionary (**kwargs)
'''
def make_sentence(**kwargs):
    sen = ""
    for i in kwargs.values(): #loop in values of dictionry
        sen += i              #without . values ==> print only keys of dictionry
    return sen
print (make_sentence(a="Ahmed ",b="is ",c="a ",d="man"))
'''

def make_dict(**kwargs):
    
    for key, value in kwargs.items(): #loop in key and value of dictionry
        print(f"{key} : {value}")             #without . values ==> print only keys of dictionry
    
print (make_dict(a="Ahmed ",b="is ",c="a ",d="man"))
