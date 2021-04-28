import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser(
    description="Lab two - Visualisation")
parser.add_argument('--graph', help="deltoid, galilean, fey")

graph = parser.parse_args().graph

if graph == 'deltoid':
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)

    plt.plot(x, y)
    plt.xlabel(r"$2cos(\theta) + cos(2\theta)$")
    plt.ylabel(r"$2sin(\theta) - sin(2\theta)$")
    plt.title("Deltoid curve")
    plt.show()
elif graph == 'galilean':
    theta = np.linspace(0, 10 * np.pi, 1000)
    r = 2 * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.plot(x, y)
    plt.xlabel(r"$rcos(\theta)$")
    plt.ylabel(r"$rsin(\theta)$")
    plt.title("Galilean Spiral")
    plt.show()
elif graph == 'fey':
    theta = np.linspace(0, 12 * np.pi, 1000)

    x = np.sin(theta) * ((np.e ** np.cos(theta)) -
                        (2 * np.cos(4 * theta)) + (np.sin(theta / 12) ** 5))
    y = np.cos(theta) * ((np.e ** np.cos(theta)) -
                        (2 * np.cos(4 * theta)) + (np.sin(theta / 12) ** 5))

    plt.plot(x, y)
    plt.title("Fey's Function")
    plt.show()
else:
    parser.print_help()
