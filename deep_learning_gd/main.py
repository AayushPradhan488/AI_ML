from sgd_new import *
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

output = do_sgd(x, y, 5, 0.5, 0.1, 0.01)

plt.plot(x,[z[0] for z in output])
plt.show()