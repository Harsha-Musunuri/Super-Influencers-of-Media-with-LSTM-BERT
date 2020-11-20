import statistics

from kneed import KneeLocator


def identify_knee_points(x, y):
    knees = []
    for i in range(1, len(x)):
        kl = KneeLocator(x[:i + 1], y[:i + 1], curve='convex', direction="increasing", S=5)
        knees.append(kl.knee)
    return statistics.mode(knees)


def identify_single_knee_point(x, y, plot=False):
    kl = KneeLocator(x, y, curve='convex', direction="increasing", S=5)
    if plot:
        kl.plot_knee()
    return kl.all_knees


def execute_knee():
    y = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 5, 9, 25, 80, 190, 220, 230, 250, 260, 265, 266, 267, 268]
    print(len(y))
    x = [i + 1 for i in range(len(y))]
    print(identify_knee_points(x, y))


if __name__ == '__main__':
    execute_knee()
