import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import random

figure = plt.figure()
canvas = FigureCanvas(figure)


def graphic():
    estoque = 150
    saida = 93

    labels = "Estoque", "Saidas"
    sizes = [estoque, saida]
    fig1, axl = plt.subplots()
    axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axl.axis("equal")

    plt.show()

def plotbar():
    fruits = ['aplles', 'oranges', 'coconuts', 'pawpaw']
    values = random.randint(50, size=4)
    print(values)

    plt.bar(fruits, values, color='red', width=0.4)

    plt.xlabel('Type of Fruits')
    plt.ylabel('No. Of Fruits')
    plt.title('Random Fruits in my Basket')

    canvas.draw()



plotbar()


graphic()