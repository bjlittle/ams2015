import matplotlib.pyplot as plt
import os

import cartopy.crs as ccrs
from cartopy.io.img_tiles import MapQuestOpenAerial
import iris


dname = '/project/avd/iris/presentations/um_user_tutorial'
fname = os.path.join(dname, 'data', 'MERRA300.prod.assim.tavg1_2d_slv_Nx.20131109.hdf.nc')
v, u = iris.load(fname)

plt.figure(figsize=(16, 12))

map_quest_aerial = MapQuestOpenAerial()
ax = plt.axes(projection=map_quest_aerial.crs)
ax.set_extent((90, 140, -15, 30), crs=ccrs.PlateCarree())

ax.add_image(map_quest_aerial, 8)
ax.coastlines(resolution='50m', color='wheat')

clon = iris.Constraint(longitude=lambda cell: 90 < cell.point < 140)
clat = iris.Constraint(latitude=lambda cell: -15 < cell.point < 30)
v = v.extract(clon & clat)
u = u.extract(clon & clat)

x = v.coord('longitude').points
y = v.coord('latitude').points

ax.quiver(x, y, u[0].data, v[0].data, scale=20, regrid_shape=55, scale_units='inches',
          width=0.0015, transform=ccrs.PlateCarree(), color='white')

x, y = [105.4, 105.4, 116.53, 116.53, 105.40], [12.71, 23.3, 23.3, 12.71, 12.71]
ax.plot(x, y, transform=ccrs.PlateCarree(), color='yellow')
ax.fill(x, y, color='coral', transform=ccrs.PlateCarree(), alpha=0.3)

tcoord = v[0].coord('time')
t = tcoord.units.num2date(tcoord.points[0])
title = 'Hurricane Haiyan, Category 5 Super Typhoon {}'.format(t)
ax.set_title(title, fontsize=16)

plt.savefig('mapquest_quiver.png', transparent=True)
plt.show()
