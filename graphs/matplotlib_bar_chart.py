# bar_chart.py

import matplotlib.pyplot as plt

def bar_chart(numbers, labels, pos):
    fig = plt.figure(figsize=(5, 8))
    plt.bar(pos, numbers, color='blue')
    plt.xticks(ticks=pos, labels=labels)
    plt.show()

if __name__ == '__main__':
    numbers = [2, 1, 4, 6]
    labels = ['Electric', 'Solar', 'Diesel', 'Unleaded']
    pos = list(range(4))
    bar_chart(numbers, labels, pos)