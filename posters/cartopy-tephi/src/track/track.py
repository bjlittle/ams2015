import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import shapely.geometry as sgeom

import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.io.shapereader as cshp


def sample_data():
    """
    Returns a list of latitudes and a list of longitudes (lons, lats)
    for Hurricane Katrina (2005).

    The data was originally sourced from the HURDAT2 dataset from AOML/NOAA:
    http://www.aoml.noaa.gov/hrd/hurdat/newhurdat-all.html on 14th Dec 2012.

    """
    lons = [-75.1, -75.7, -76.2, -76.5, -76.9, -77.7, -78.4, -79.0,
            -79.6, -80.1, -80.3, -81.3, -82.0, -82.6, -83.3, -84.0,
            -84.7, -85.3, -85.9, -86.7, -87.7, -88.6, -89.2, -89.6,
            -89.6, -89.6, -89.6, -89.6, -89.1, -88.6, -88.0, -87.0,
            -85.3, -82.9]

    lats = [23.1, 23.4, 23.8, 24.5, 25.4, 26.0, 26.1, 26.2, 26.2, 26.0,
            25.9, 25.4, 25.1, 24.9, 24.6, 24.4, 24.4, 24.5, 24.8, 25.2,
            25.7, 26.3, 27.2, 28.2, 29.3, 29.5, 30.2, 31.1, 32.6, 34.1,
            35.6, 37.0, 38.6, 40.1]

    return lons, lats


fig = plt.figure(figsize=(16, 12))
ax = plt.axes(projection=ccrs.LambertConformal())

ax.background_patch.set_visible(False)
ax.outline_patch.set_visible(False)

lakes = cfeat.NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='grey', facecolor='none')
ax.add_feature(lakes)

# Download from naturalearthdata.com the file containing world-wide transportation networks ...
roads = cfeat.NaturalEarthFeature(category='cultural',
                                  name='roads',
                                  scale='10m',
                                  facecolor='none', edgecolor='lightgrey')

ax.add_feature(roads)

usa = (-130, -65, 15, 50)
ax.set_extent(usa, crs=ccrs.Geodetic())
ax.coastlines('50m', color='grey')

lons, lats = sample_data()
track = sgeom.LineString(list(zip(lons, lats)))

track_buffer = track.buffer(2)
ax.add_geometries([track_buffer], ccrs.PlateCarree(), facecolor='wheat', alpha=0.5)

fname = cshp.natural_earth(category='cultural',
                           name='roads',
                           resolution='10m')

for road in cshp.Reader(fname).geometries():
    edgecolor = None
    if road.intersects(track):
        edgecolor = 'red'
    elif road.intersects(track_buffer):
        edgecolor = 'green'
    if edgecolor is not None:
        ax.add_geometries([road], ccrs.PlateCarree(), facecolor='none', edgecolor=edgecolor)
        
ax.add_geometries([track], ccrs.PlateCarree(), facecolor='none', edgecolor='blue', linewidth=2)

x, y = [-85.8, -85.8, -76.25, -76.25, -85.8], [23.14, 29.35, 29.35, 23.14, 23.14]
ax.plot(x, y, transform=ccrs.PlateCarree(), color='black')

plt.title('U.S. transportation routes which intersect the track '
          'of Hurricane Katrina (2005)')

direct_hit = mpatches.Rectangle((0, 0), 1, 1, facecolor='red')
within_2_deg = mpatches.Rectangle((0, 0), 1, 1, facecolor='green')
labels = ['Route directly intersects with track',
          'Route is within 2 degrees of track']
plt.legend([direct_hit, within_2_deg], labels,
           loc='lower right', fancybox=True)

plt.savefig('track.png', transparent=True)
plt.show()
