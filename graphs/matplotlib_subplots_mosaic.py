import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
axd['upleft'].set_title('upleft')
axd['upleft'].plot(x, y)

axd['lowleft'].set_title('lowleft')
axd['lowleft'].plot(y, x)

axd['right'].set_title('right')
plt.show()