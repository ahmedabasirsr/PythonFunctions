##############Dunder Function#################
##            Duplicate Under                ##
##############################################
x = "Svetozar Mrkovic"
y = ["first", "second"]
print( "Print how many charachters in string x: ",len(x))
print ("Print second element in list y: ",y[1])

##############Bulit in function################
##                len and []                  ##
###############################################

print (" len works through dunder function __len__ :",x.__len__())
# x.__len__() absolutely same len(x)
print("###############################################")
print (" [] works through dunder function __getitem__ :",y.__getitem__(1))
# y.__getitem__(1) absolutely same y[1]
print("###############################################")
print ("How I know what are methods that object use: ",dir(x))
print(x.__dir__())
# x.__dir__(1) absolutely same dir(x)

