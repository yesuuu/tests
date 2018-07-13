import matplotlib.pyplot as plt
import sys
sys.path.append('/home/fanruoxin/rx_tools')
from rx_tools import RxTools
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


r2_is = []
r2_os = []

for i in range(100):
    size = 200000
    n1 = stats.norm.rvs(size=size)
    n2 = stats.norm.rvs(size=size)
    # n3 = stats.norm.rvs(size=10000)

    x = n1
    y = 0.3 * n1 + n2

    train_len = int(5./8 * size)
    test_len = int(3./8 * size)
    x_train = x[:train_len].reshape((-1, 1))
    y_train = y[:train_len]
    x_test = x[train_len:(train_len + test_len)].reshape((-1, 1))
    y_test = y[train_len:(train_len + test_len)]

    model = LinearRegression(fit_intercept=False, normalize=False)

    model.fit(x_train, y_train)

    y_hat_train = model.predict(x_train)
    y_hat_test = model.predict(x_test)

    r2_train = RxTools.OneDAnalysisFunctions.calc_outr2(y_train, y_hat_train)
    r2_test = RxTools.OneDAnalysisFunctions.calc_outr2(y_test, y_hat_test)

    r2_is.append(r2_train)
    r2_os.append(r2_test)
    print '_' * 50
    print 'in sample r2:', r2_train
    print 'out sample r2:', r2_test

plt.plot(r2_is, label='is')
plt.plot(r2_os, label='os')
plt.legend(loc='best')
plt.show()

m = [i for i in range(len(r2_os)) if r2_is[i] <= r2_os[i]]
print len(m)


print 'is mean:', np.mean(r2_is)
print 'is std:', np.std(r2_is)
print 'os mean:', np.mean(r2_os)
print 'os std:', np.std(r2_os)