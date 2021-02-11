import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser(
    description="Lab two - Visualisation")
parser.add_argument('--graph', help="deltoid, galilean, fey")

graph = parser.parse_args().graph

"""
  a)  Make a plot of the so-called deltoid curve, which is defined parametrically by 
  the equations, x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. Take 
  a set of values of θ between zero and 2π and calculate x and y for each from the 
  equations above, then plot y as a function of x.
  b)  Taking this approach a step further, one can make a polar plot r = f(θ) for some 
  function f by calculating r for a range of values of θ and then converting r and θ 
  to Cartesian coordinates using the standard equations x = r cos θ, y = r sin θ. Use 
  this method to make a plot of the Galilean spiral, r=θ2 for 0 ≤ θ ≤ 10π.
  c)  Using the same method, make a polar plot of “Fey’s function”
  r = e^(cos(θ)) - 2 cos(4 * θ) + sin^5(θ/12) in the range 0 ≤ θ ≤ 24π.
"""

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
