import os
import sys
import pandas as pd
import numpy as np
from descartes import PolygonPatch
import matplotlib.pyplot as plt
import trimesh as tm

sys.path.insert(0, os.path.dirname(os.getcwd()))

import alphashape
import point_cloud_utils as pcu

# Import points from the point cloud as numpy array
base_path = "/home/geoailab/Downloads/point2mesh-20240411T065451Z-001/point2mesh/z/"
file_name = "face.ply"
points_3d = pcu.loadCloudFromPLY(base_path+file_name)

alpha_shape = alphashape.alphashape(points_3d,0.00001)

# Exporting the Alpha Shape (Trimesh Object)
obj = tm.exchange.obj.export_obj(alpha_shape, include_normals=True, include_color=True, include_texture=True, return_texture=False, write_texture=True, resolver=None, digits=8, header='https://github.com/mikedh/trimesh')

alphashape_path = base_path+"face.obj"
f = open(alphashape_path, "w")
f.write(obj)
f.close()

# Generating the Init Mesh from the Alpha Shape

os.system("/home/geoailab/Downloads/point2mesh-20240411T065451Z-001/point2mesh/manifold "+alphashape_path+" "+"/".join(alphashape_path.split("/")[0:-1])+"/init_mesh.obj"+" 3000")

#alpha_shape.show()




