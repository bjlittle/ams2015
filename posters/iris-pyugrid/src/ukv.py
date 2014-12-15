import matplotlib.pyplot as plt

import cartopy.crs as ccrs
from cartopy.io.img_tiles import MapQuestOpenAerial
import iris
import iris.plot as iplt


fname = '../data/ukVpmslont_first_field.pp'
cube = iris.load_cube(fname)

# Decimate the cube ...
cube = cube[::20, ::20]

fig = plt.figure(figsize=(16, 12))
map_quest_aerial = MapQuestOpenAerial()
#ax = plt.axes(projection=ccrs.Mercator())
ax = plt.axes(projection=map_quest_aerial.crs)

iplt.pcolormesh(cube, edgecolor='grey', linewidth=1)

ax.add_image(map_quest_aerial, 8)
ax.coastlines(resolution='10m')
ax.outline_patch.set_edgecolor('none')
#ax.set_extent((-16.91, 8.05, 46.29, 61.35), crs=ccrs.PlateCarree())
ax.set_extent((-29, 19, 37, 66), crs=ccrs.PlateCarree())

#plt.savefig('ukv.png', transparent=True, dpi=200)
plt.show()
