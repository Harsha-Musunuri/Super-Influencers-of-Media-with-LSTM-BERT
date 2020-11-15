import matplotlib.pyplot as plt
from kneed import KneeLocator


def identify_knee_points_incremental(x, y):
    """
    Incomplete. Using this to solve the flat ends issue
    :param x:
    :param y:
    :return:
    """
    knees = []
    for i in range(1, len(x)):
        kl = KneeLocator(x[:i + 1], y[:i + 1], curve='convex', direction="increasing", S=5)
        knees.append(kl.knee)
    return knees


def identify_single_knee_point(x, y, show_plot=False):
    kl = KneeLocator(x, y, curve='convex', direction="increasing", S=5)
    if show_plot:
        kl.plot_knee()
        plt.show()
    return kl.knee


def execute_knee():
    y = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 5, 9, 25, 80, 190, 220, 230, 250, 260]
    print(len(y))
    x = [i + 1 for i in range(len(y))]
    print(identify_single_knee_point(x, y, show_plot=True))


if __name__ == '__main__':
    execute_knee()
