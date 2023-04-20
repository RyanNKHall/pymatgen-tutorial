from pymatgen.ext.matproj import MPRester # MPRestError
from mp_api.client.core.client import MPRestError
from pymatgen.electronic_structure.plotter import BSPlotter
import numpy as np
import matplotlib.pyplot as plt

API_KEY = "" # PUT YOUR API KEY HERE AS A STRING

# Import a band structure by mpid
mpid = "mp-149" # Si

with MPRester(API_KEY) as mp:
    bs = mp.get_bandstructure_by_material_id(mpid)

bs_plot = BSPlotter(bs)
bs_plot.get_plot().show()

# plot the BZ
B = bs.lattice_rec.matrix # reciprocal lattice vectors
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_box_aspect((1,1,1))

for face in bs.lattice_rec.get_wigner_seitz_cell():
    face = np.take(np.asarray(face), range(0,len(face)+1), mode='wrap', axis=0)
    ax.plot(face[:,0], face[:,1], face[:,2], color='r', linewidth=1)
    ax.scatter(face[:,0], face[:,1], face[:,2], color='r', s=20)

xyzlim = np.array([ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()]).T
XYZlim = [min(xyzlim[0]), max(xyzlim[1])]
ax.set_xlim3d(XYZlim)
ax.set_ylim3d(XYZlim)
ax.set_zlim3d(XYZlim)

plt.show()





