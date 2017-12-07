import shapely.geometry as sg
import matplotlib.pyplot as plt
import descartes


def plot_circles(x, y, score, ofile, x_hobbies, y_hobbies):
    plt.figure()
    # create the circles with shapely
    x0 = 0

    a = sg.Point(x0 - (0.5 - score / 2), 0).buffer(1.)
    b = sg.Point(x0 + (0.500001 - score / 2), 0).buffer(1.)

    # a = sg.Point(x0 - 0.5, 0).buffer(1.)
    # b = sg.Point(x0 + 0.5, 0).buffer(1.)

    # compute the 3 parts
    left = a.difference(b)
    right = b.difference(a)
    middle = a.intersection(b)

    # use descartes to create the matplotlib patches
    ax = plt.gca()
    ax.add_patch(descartes.PolygonPatch(left, fc='b', ec='k', alpha=0.2))
    ax.add_patch(descartes.PolygonPatch(right, fc='r', ec='k', alpha=0.2))
    ax.add_patch(descartes.PolygonPatch(middle, fc='g', ec='k', alpha=0.2))
    plt.gca().text(-0.7, 1.5, x, fontsize=15, horizontalalignment='center', alpha=0.5, color='b')
    plt.gca().text(0.7, 1.5, y, fontsize=15, horizontalalignment='center', alpha=0.5, color='r')
    plt.gca().text(0, -1.5, round(score, 2), fontsize=15, horizontalalignment='center', alpha=0.5, color='g')

    plt.gca().text(0, 0, '\n'.join(x_hobbies & y_hobbies), fontsize=15, horizontalalignment='center', alpha=0.5, color='g')

    # control display
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    plt.savefig(ofile, dpi=300)
    # plt.show()
    plt.close()


if __name__ == '__main__':
    x, y, score = 'Аня', 'Боря', 0.666666
    print(x, y, score)
    ofile = rf'img/{x}{y}{score:0.2f}.png'
    x_hobbies = {'вино', 'кино', 'музыка'}
    y_hobbies = {'домино', 'кино', 'музыка'}
    plot_circles(x, y, score, ofile, x_hobbies, y_hobbies)
    print(ofile)
