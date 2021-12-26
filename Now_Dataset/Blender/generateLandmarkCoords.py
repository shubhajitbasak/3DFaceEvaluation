import bpy
import sys
import numpy as np
import os

objpath = sys.argv[-1]
# objFilePath = '/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBase/FaMoS_180424_03335_TA/multiview_expressions/IMG_0053.obj'

npypath = objpath.replace('.obj', '.npy')
if os.path.exists(npypath):
    os.remove(npypath)

vertices_bfm = [1959, 6214, 10076, 14197, 8203, 5780, 10794]
vertex_pos = []

# Import OBJ
bpy.ops.import_scene.obj(filepath=objpath)

obj = bpy.context.selected_objects[0]

for id, vert in enumerate(vertices_bfm):
    vertex_pos.append(obj.data.vertices[vert].co)
print(np.array(vertex_pos).shape)
np.save(npypath, np.array(vertex_pos))
