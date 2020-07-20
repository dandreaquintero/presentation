from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

import numpy as np
import matplotlib.pyplot as plt

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

m = Basemap(projection='cyl',llcrnrlat=-3,urcrnrlat=13,
                llcrnrlon=280,urcrnrlon=292,resolution='h')

m.drawcoastlines(color='black',linewidth=1)
# m.drawparallels([45],labels=[1,1,0,1], fontsize=8)
# m.drawparallels([0],labels=[1,1,0,1], fontsize=8, linewidth=2, color='k')
# m.drawmeridians([-75, -35,  5],labels=[1,1,0,1], rotation=45, fontsize=8)
#
# m.fillcontinents(color="#FFDDCC", lake_color='#DDEEFF')
# m.drawmapboundary(fill_color="#DDEEFF")
m.drawcountries(color='black', linewidth=1)
#m.shadedrelief(ax=None, scale=None, origin='higher')
#m.bluemarble(resolution='h')
m.etopo()
plt.show()
