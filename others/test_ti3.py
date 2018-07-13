def test(num, numList=[]):
    numList.append(num)
    return numList

a = test(1)
b = test(2, a)
c = test(3)
print c