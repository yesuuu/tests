import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.1)
y = np.abs(x) - 0.5

from ruoxin_util import RxModeling

m = RxModeling.Fitting.PiecewiseReg([0])
m.fit(x, y)

yHat = m.predict(x)
plt.plot(x, yHat)