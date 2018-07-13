def testA(a=1, **kwargs):
    print a
    print kwargs

testA(b=1, c=1)
testA(a=10, b=1)