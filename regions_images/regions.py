from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

import numpy as np
import matplotlib.pyplot as plt

def draw_screen_poly(box_in, m):
    '''
    '''
    import numpy as np
    from matplotlib.patches import Polygon

    import matplotlib.pyplot as plt

    # to draw polygon
    lon0 = box_in[0]
    lon1 = box_in[1]
    lat0 = box_in[2]
    lat1 = box_in[3]
    resolution = 10
    lats_r = np.hstack((np.linspace(lat0, lat1, resolution),
                        np.linspace(lat1, lat0, resolution)))

    lons_r = np.hstack((np.linspace(lon0, lon0, resolution),
                        np.linspace(lon1, lon1, resolution)))

    x, y = m(lons_r, lats_r)
    xy = zip(x, y)
    poly = Polygon(list(xy), fc=(1, 0, 0, 0.0), ec=(0, 0, 0, 1), lw=1, zorder=5)
    plt.gca().add_patch(poly)

# fig = plt.figure()
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
#
# m = Basemap(projection='cyl',llcrnrlat=-20,urcrnrlat=70,
#                 llcrnrlon=-95,urcrnrlon=25,resolution='l')
#
# m.drawcoastlines(color='gray',linewidth=0.25)
# m.drawparallels([45],labels=[1,1,0,1], fontsize=8)
# m.drawparallels([0],labels=[1,1,0,1], fontsize=8, linewidth=2, color='k')
# m.drawmeridians([-75, -35,  5],labels=[1,1,0,1], rotation=45, fontsize=8)
#
# m.fillcontinents(color="#FFDDCC", lake_color='#DDEEFF')
# m.drawmapboundary(fill_color="#DDEEFF")
# m.drawcountries(color='gray', linewidth=0.25)
# patches = []
# zone_A = np.array([[6, 48.5],[15,48.5],[15,44],[6,44]])
#
# zone_B = np.array([[282-360,9.5],[288-360,9.5],[288-360,0.5],[282-360,0.5]])
#
# patches.append(Polygon(zone_A))
# patches.append(Polygon(zone_B))
#
# ax.add_collection(PatchCollection(patches, facecolor='lightgreen', edgecolor='k', linewidths=0.5, zorder=5, alpha=0.5))
#
# # plt.title('Regioni di studio', fontsize=8)
# #
# # plt.xlabel('Longitude', labelpad=40, fontsize=8)
# # plt.ylabel('Latitude', labelpad=40, fontsize=8)
#
# plt.savefig('regionsmap.pdf', bbox_inches='tight')


fig = plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(projection='cyl',llcrnrlat=-2,urcrnrlat=12, llcrnrlon=278,urcrnrlon=297, resolution='i')
m.drawcountries(color='gray', linewidth=1)
m.drawcoastlines(color='gray',linewidth=1)
m.arcgisimage(service='World_Physical_Map', xpixels = 2000, verbose= True)

patches = []
zone_B = np.array([[282,9],[288,9],[288,0.5],[282,0.5]])
patches.append(Polygon(zone_B))

ax.add_collection(PatchCollection(patches, facecolor=(1, 0, 0, 0), edgecolor='k', linewidths=1, zorder=5))
plt.savefig('andes.pdf', bbox_inches='tight', dpi=200)
# plt.show()
plt.close()


fig = plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(projection='merc',llcrnrlat=43,urcrnrlat=49.5, llcrnrlon=3.5,urcrnrlon=16.5, resolution='i', epsg=3002)
m.drawcountries(color='gray', linewidth=1)
m.drawcoastlines(color='gray',linewidth=1)
m.arcgisimage(service='World_Physical_Map', xpixels = 2000, verbose= True)

draw_screen_poly([5.5, 14.5, 44, 48.5], m)

# plt.show()
plt.savefig('alpin.pdf', bbox_inches='tight')
plt.close()
