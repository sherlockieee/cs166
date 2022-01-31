import matplotlib

matplotlib.use("TkAgg")
from pylab import *

n = 100  # size of space: n x n
p = 0.1  # probability of initially panicky individuals
density = []


def set_probability(val=p):
    global p
    p = float(val)
    return val


def initialize():
    global config, nextconfig, density, p
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    density = []
    density.append(sum(config) / (n * n))


def observe():
    global config, nextconfig, density
    cla()
    subplot(1, 2, 1)
    imshow(config, vmin=0, vmax=1, cmap=cm.binary)
    subplot(1, 2, 2)
    plot(density)
    xlabel("Steps")
    ylabel("Density of state 1")


def update():
    global config, nextconfig, density
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            nextconfig[x, y] = 1 if count >= 4 else 0
    density.append(sum(nextconfig) / (n * n))
    config, nextconfig = nextconfig, config


import pycxsimulator

pycxsimulator.GUI(parameterSetters=[set_probability]).start(
    func=[initialize, observe, update]
)
