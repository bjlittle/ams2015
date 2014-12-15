import cartopy.crs as ccrs
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 12))

ax = plt.axes(projection=ccrs.Orthographic(central_longitude=-102.5))
ax.coastlines(resolution='50m')

# Add WMS layer using temperature data from NOAA.
url = 'http://gis.srh.noaa.gov/arcgis/services/NDFDTemps/MapServer/WMSServer'
layer = '0'

from cartopy.feature import LAND, OCEAN
ax.add_feature(LAND, zorder=0)
ax.add_feature(OCEAN, zorder=0)

ax.add_wms(url, layer)

plt.title('NOAA WMS NDFDTemps (Day0maxT)')

plt.savefig('noaa_wms_ortho.png', transparent=True)
plt.show()
