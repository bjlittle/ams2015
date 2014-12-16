import cartopy.crs as ccrs
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 12))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines(resolution='50m')

# Add WMS layer using temperature data from NOAA.
url = 'http://gis.srh.noaa.gov/arcgis/services/NDFDTemps/MapServer/WMSServer'
layer = '0'

from cartopy.feature import LAND, OCEAN
ax.add_feature(LAND, zorder=0)
ax.add_feature(OCEAN, zorder=0)

ax.add_wms(url, layer)
ax.set_extent((-130, -65, 15, 50), crs=ccrs.PlateCarree())

plt.title('NOAA WMS NDFDTemps (Day0maxT)')

#plt.savefig('noaa_wms.png', transparent=True)
plt.show()
