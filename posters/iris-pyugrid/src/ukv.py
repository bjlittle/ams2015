import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import iris
import iris.plot as iplt


fname = '../data/ukVpmslont_first_field.pp'
cube = iris.load_cube(fname)

# Decimate the cube ...
cube = cube[::20, ::20]

fig = plt.figure(figsize=(16,12))
ax = plt.axes(projection=ccrs.Mercator())

iplt.pcolormesh(cube, edgecolor='grey')

ax.coastlines(resolution='50m')
ax.set_extent((-16.91, 8.05, 46.29, 61.35), crs=ccrs.PlateCarree())

#plt.savefig('ukv.png', transparent=True, dpi=200)
plt.show()
