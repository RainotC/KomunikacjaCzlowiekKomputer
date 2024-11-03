import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource


def load_dem(file_path):
    with open(file_path, 'r') as file:
        # Read the first line with metadata
        w, h, d = map(int, file.readline().strip().split())
        # Read the rest as a 2D height map
        data = np.array([list(map(float, line.split())) for line in file])
    return data, w, h, d

dem_data, width, height, distance = load_dem('big.dem')


elevation_normalized = (dem_data - np.min(dem_data)) / (np.max(dem_data) - np.min(dem_data))


shaded_terrain = np.zeros((*dem_data.shape, 3))

dx, dy = np.gradient(dem_data)
d_maxx = np.max(dx)
d_maxy = np.max(dy)
for i in range(dem_data.shape[0]):
    for j in range(dem_data.shape[1]):
        elev = elevation_normalized[i, j]

        if elev <= 0.5:
            r=elev*2
            g=1
            b=0
        elif elev > 0.5:
            r=1
            g=1-(elev-0.5)*2
            b = 0


        #making pixels darker
        changex = dx[i][j]
        changey = dy[i][j]

        r = r - changex/d_maxx * 0.4
        g = g - changex/d_maxx * 0.4
        b = b - changex/d_maxx * 0.4

        r = r - changey/d_maxy * 0.4
        g = g - changey/d_maxy * 0.4
        b = b - changey/d_maxy * 0.4
        shaded_terrain[i, j] = [r, g, b]


plt.figure(figsize=(10, 10))
plt.imshow(shaded_terrain)
plt.show()