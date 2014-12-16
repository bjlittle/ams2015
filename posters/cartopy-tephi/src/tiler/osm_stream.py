import matplotlib.pyplot as plt
import os

import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM
import iris


dname = '/project/avd/iris/presentations/um_user_tutorial'
fname = os.path.join(dname, 'data', 'MERRA300.prod.assim.tavg1_2d_slv_Nx.20131109.hdf.nc')
v, u = iris.load(fname)

plt.figure(figsize=(16, 12))

osm = OSM()

ax = plt.axes(projection=osm.crs)
ax.set_extent((105.40, 116.53, 12.71, 23.30), crs=ccrs.PlateCarree())

ax.add_image(osm, 6)
ax.coastlines(resolution='10m', color='grey')

clon = iris.Constraint(longitude=lambda cell: 90 < cell.point < 140)
clat = iris.Constraint(latitude=lambda cell: -15 < cell.point < 30)
v = v.extract(clon & clat)
u = u.extract(clon & clat)

x = v.coord('longitude').points
y = v.coord('latitude').points

#ax.quiver(x, y, u[0].data, v[0].data, scale=20, regrid_shape=30, scale_units='inches',
#          width=0.0015, transform=ccrs.PlateCarree(), color='black')

#ax.barbs(x, y, u[0].data, v[0].data, regrid_shape=50, transform=ccrs.PlateCarree(), color='black')

u0, v0 = u[0].data, v[0].data

speed = (u0 * u0 + v0 * v0) ** 0.5
lw = 5 * speed / speed.max()
ax.streamplot(x, y, u0, v0, color=u0, linewidth=lw, transform=ccrs.PlateCarree())

tcoord = v[0].coord('time')
t = tcoord.units.num2date(tcoord.points[0])
title = 'Hurricane Haiyan, Category 5 Super Typhoon {}'.format(t)
ax.set_title(title, fontsize=16)

plt.savefig('osm_stream.png', transparent=True)
plt.show()
