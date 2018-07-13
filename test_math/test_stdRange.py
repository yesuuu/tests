import numpy as np
import matplotlib.pyplot as plt

n = 8
testNum = 100000

results = []
tests = []
for i in range(testNum):
    data = np.random.rand(n) * 2 - 1
    result = (data[0] - np.mean(data)) / np.std(data)
    results.append(result)
    tests.append(data)

plt.hist(results, bins=100)
plt.show()