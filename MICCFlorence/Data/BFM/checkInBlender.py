import bpy
import numpy as np

vertices_bfm = np.load('/MICCFlorence/Data/BFM/landmark_ids_bfm.pkl', allow_pickle=True)

bpy.ops.object.mode_set(mode = 'OBJECT')
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')

ob = bpy.data.objects['bfm_model_front']

vertex_pos = []

for vert in vertices_bfm:
    ob.data.vertices[vert].select = True
    vertex_pos.append(ob.data.vertices[vert].co)

bpy.ops.object.mode_set(mode = 'EDIT')

print(vertex_pos)

np.save('/MICCFlorence/Data/BFM/landmark_ids_loc.npy', vertex_pos)