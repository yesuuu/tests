a = 1
b = 100
c = 0
for i in range(7):
    c = (a + b) * 1. / 2
    if a == c or b == c:
        break
    a = b
    b = c

print c