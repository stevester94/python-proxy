# kwargs testing

import functools



def fun(A, B, C):
    print("A: " + str(A))
    print("B: " + str(B))
    print("C: " + str(C))

# Single star testing
print("\nSingle star")
l = {1, 2, 3}
fun(*l)

# double star testing
print("\nDouble star")
d = {"A": 13, "B": 15, "C": 16}
fun(**d)


# 13 and 14 will be permanently tied to A and B for newFun  
print("\nPartial")
newFun = functools.partial(fun, 13, 14)
newFun(18)

# Args just use position and produce a list, they cannot be named
# convention to use *args but its literally anything
def argFun(A, *couldBeCalledAnything):
  print("A: " + str(A))
  print(couldBeCalledAnything)
  
print("\nArg testing")
argFun(13, 500, 600, "kek")


# convention to use *kargs but its literally anything
def kargFun(A, **couldBeCalledAnything):
  print("A: " + str(A))
  print(couldBeCalledAnything)

print("\nkarg testing")
# For kargs (keyword args), they HAVE to have a parameter specified
kargFun(13, T=500, P=600, D="jej")
