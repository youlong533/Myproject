import timeit
def test1():
    l = [i for i in range(1000)]

t1 = timeit.Timer("test1()", "from __main__ import test1")
print(t1.timeit(number=1000))


popzero = timeit.Timer("x.pop(0)","from __main__  import x")
popend = timeit.Timer("x.pop()","from __main__  import x")

print("pop(0) pop()")

for i in range(1000,10001,100):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz,pt))
