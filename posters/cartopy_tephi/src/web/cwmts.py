import matplotlib.pyplot as plt

import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature

lakes = NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='y', facecolor='none')

fig = plt.figure(figsize=(16, 12))

ax = plt.axes(projection=ccrs.PlateCarree())

url = 'http://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi'
layer = 'VIIRS_CityLights_2012'
ax.add_wmts(url, layer)
ax.coastlines(resolution='50m', color='y')
ax.add_feature(lakes)
ax.set_extent((-130, -65, 15, 50))

plt.title('Suomi NPP Earth at night April/October 2012')

plt.savefig('lights.png', transparent=True, dpi=200)
plt.show()
