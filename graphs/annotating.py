# Example from: https://www.analyticsvidhya.com/blog/2020/05/10-matplotlib-tricks-data-visualization-python/

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(8,6))

X = list(range(10))
plt.plot(X, np.exp(X))
plt.title('Annotating Exponential Plot using plt.annotate()')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.annotate('Point 1', xy=(6,400),
             arrowprops=dict(arrowstyle='->'),
             xytext=(4,600))

plt.annotate('Point 2', xy=(7,1150),
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3,rad=-.2'),
             xytext=(4.5,2000))

plt.annotate('Point 3', xy=(8,3000),
             arrowprops=dict(arrowstyle='-|>',
                             connectionstyle='angle,angleA=90,angleB=0'),
             xytext=(8.5,2200))

plt.show()