# bar_chart_watermark.py

import matplotlib.pyplot as plt

def bar_chart(numbers, labels, pos):
    fig = plt.figure(figsize=(5, 8))
    plt.bar(pos, numbers, color='red')

    # add watermark
    fig.text(1, 0.15, 'Mouse vs Python',
             fontsize=45, color='blue',
             ha='right', va='bottom', alpha=0.4,
             rotation=25)

    plt.xticks(ticks=pos, labels=labels)
    plt.show()

if __name__ == '__main__':
    numbers = [2, 1, 4, 6]
    labels = ['Electric', 'Solar', 'Diesel', 'Unleaded']
    pos = list(range(4))
    bar_chart(numbers, labels, pos)