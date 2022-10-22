"""
def Ali(arg,result=[]):
    result.append(arg)
    print(result)

Ali("a")
Ali("b")
Ali("c")
"""
def for_li(*arg,result=[]):
    result.append(arg)
    print("\n",result)

for_li(4,5,6)
def form_li1(*arg,result=[]):
    for i in arg:
        result.append(i)
    print(result)
form_li1(5,6,7)

