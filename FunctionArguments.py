def argument(a,b):
    # function has 2 arguments.they aryuments will be any object
    # (int,float,string,list,dictionary,tuple,...)
    return a,b
    # return a and b togther in format tuple (a,b)

x,y = argument([1,2,3,4],(9,8,7))
# argumentes are list and tuple
print(x,y)

z,r = argument({"a":1, "b":2, "c":3},[[1,2],[3,4],[5,6]])
# argumentes are dictionary and nested list
print(z,r)

g,m = argument("string",55)
# argumentes are string and integer
print(m,g)

g,m =argument(99,"string")
#order of arguments dosnot matter
print(g,m)