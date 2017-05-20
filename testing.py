# kwargs testing

import functools



def fun(A, B, C):
    print "A: " + str(A)
    print "B: " + str(B)
    print "C: " + str(C)

# Single star testing
l = {1, 2, 3}
fun(*l)

# double star testing
d = {"A": 13, "B": 15, "C": 16}
fun(**d)

# 13 and 14 will be permanently tied to A and B for newFun  
newFun = functools.partial(fun, 13, 14)




