# simple_tide.py
# Max Liang
# created 12/27/2022
# Description:
# Calculate the diurnal tide at the equator. 
# Animate the result in a daily circle.



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# function to calculate tide height
def analytic_equator(frame, N):
    G = 1
    M = 1
    a = 2
    h = 1
    D = 1
    g = 1
    h = 1
    w = 1
    numerator = 3 * G * M * a **(2) * h
    denominator = 4 * D ** (3) * (g * h - (w * a) ** (2))
    osc_terms = []
    circle = np.linspace(0, 2 * np.pi, N)
    for n in circle:
        osc_terms.append(np.cos(w * n + frame) ** (2))
    return numerator * np.array(osc_terms) / denominator


# define function to update bar_container 
def prepare_animation(bar_container):

    def animate(frame):
        radii = analytic_equator(frame, N)
        radii -= radii.min()
        width = (2 * np.pi) / N
        for r, rect in zip(radii, bars):
            rect.set_height(r)
        return radii

    return animate


# Initialize box_container object
N = 200
bottom = 4
max_height = 4
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = np.random.rand(N)
width = (2 * np.pi) / N
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set(title="Daily Tide at Equator Plane")
bars = ax.bar(theta, radii, width=width, bottom=bottom)


ani = FuncAnimation(fig, prepare_animation(bars), frames=np.linspace(0, 2 * np.pi, 150), blit=True)

plt.show()

