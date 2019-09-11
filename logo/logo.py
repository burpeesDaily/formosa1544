"""Generate the Logo."""
import matplotlib
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D

earthquake_data = pd.read_csv(
    "earthquake.csv", sep=",", header=None,
    names=["longitude", "latitude", "magnitude", "depth"])

longitude = earthquake_data.longitude
latitude = earthquake_data.latitude
magnitude = earthquake_data.magnitude
depth = -earthquake_data.depth
color = magnitude * 100

normalize = colors.Normalize(vmin=200, vmax=1500)

area = (magnitude)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(xs=longitude, ys=latitude, zs=depth, c=color, s=area,
           cmap="rainbow", norm=normalize)

plt.show()
