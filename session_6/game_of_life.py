import matplotlib

matplotlib.use("TkAgg")
from pylab import *

n = 100  # size of space: n x n
density = []
p = 0.1


def initial_probability(val=p):
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
                    if dx == dy == 0:
                        continue
                    count += config[(x + dx) % n, (y + dy) % n]
            if config[x, y] == 1 and count in [2, 3]:
                nextconfig[x, y] = 1
            elif config[x, y] == 0 and count == 3:
                nextconfig[x, y] = 1
            else:
                nextconfig[x, y] = 0
    config, nextconfig = nextconfig, config
    density.append(sum(config) / (n * n))


import pycxsimulator

pycxsimulator.GUI(parameterSetters=[initial_probability]).start(
    func=[initialize, observe, update]
)
