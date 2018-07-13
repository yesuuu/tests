import numpy as np
import matplotlib.pyplot as plt


def testBoxPlot():
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)
    ax = plt.boxplot(data)
    return ax

ax = testBoxPlot()
# plt.show()