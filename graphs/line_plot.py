# line_plot.py

import matplotlib.pyplot as plt

def line_plot(numbers):
    plt.plot(numbers)
    plt.ylabel('Random numbers')
    plt.show()

if __name__ == '__main__':
    numbers = [2, 4, 1, 6]
    line_plot(numbers)
