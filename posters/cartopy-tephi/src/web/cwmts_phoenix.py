import matplotlib.patheffects as mpath
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans

import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature

lakes = NaturalEarthFeature('physical', 'lakes', '10m', edgecolor='y', facecolor='none')

fig = plt.figure(figsize=(16, 12))

ax = plt.axes(projection=ccrs.PlateCarree())

url = 'http://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi'
layer = 'VIIRS_CityLights_2012'
ax.add_wmts(url, layer)
ax.coastlines(resolution='10m', color='y')
ax.add_feature(lakes)
ax.set_extent((-119.43, -109.42, 28.72, 34.78), crs=ccrs.PlateCarree())
plt.title('Suomi NPP Earth at night April/October 2012 (Pacific Southwest Region)')

lat, lon = 33.44, -112.06
ax.scatter(lon, lat, marker=(5, 1), color='r', transform=ccrs.PlateCarree(), edgecolor='black', s=200)
#transform = ccrs.PlateCarree()._as_mpl_transform(ax) + mtrans.Affine2D().translate(25, 20)
transform = ccrs.PlateCarree()._as_mpl_transform(ax)
text_transform = mtrans.offset_copy(transform, units='dots', x=50, y=30)

plt.text(lon, lat, 'Phoenix', color='black', transform=text_transform, size=20,
         va='center', ha='left', bbox=dict(facecolor='wheat', alpha=0.5, boxstyle='round'),
         path_effects=[mpath.withStroke(linewidth=3, foreground='white')])

plt.savefig('lights_phoenix.png', transparent=True, dpi=200)
plt.show()
