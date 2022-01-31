# Simple CA simulator in Python
#
# *** Forest fire ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# Modified to run with Python 3

import matplotlib

matplotlib.use("TkAgg")

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 100
height = 100
initProb = 0.5
empty, tree, fire, char = range(4)
density = []


def init():
    global time, config, nextConfig, density

    time = 0

    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                state = tree
            else:
                state = empty
            config[y, x] = state
    config[height // 2, width // 2] = fire
    density = []

    nextConfig = SP.zeros([height, width])


def draw():
    PL.cla()
    PL.subplot(1, 2, 1)
    PL.pcolor(config, vmin=0, vmax=3, cmap=PL.cm.binary)
    PL.axis("image")
    PL.title("t = " + str(time))
    PL.subplot(1, 2, 2)
    PL.plot(density)
    PL.xlabel("Steps")
    PL.ylabel("Density of char")


def step():
    global time, config, nextConfig, width, height, density

    time += 1

    next_density = 0

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == fire:
                state = char

            elif state == tree:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y + dy) % height, (x + dx) % width] == fire:
                            state = fire

            nextConfig[y, x] = state
            next_density = (
                next_density + 1 if (state == fire or state == char) else next_density
            )

    config, nextConfig = nextConfig, config
    density.append(next_density / (width * height))


import pycxsimulator

pycxsimulator.GUI().start(func=[init, draw, step])
