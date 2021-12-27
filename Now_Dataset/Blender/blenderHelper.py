# --------- Add Empty in mesh from location of 7 keypoint ----------#

# import numpy as np
# import bpy
# import mathutils
#
#
# def load_pp(fname):
#     lamdmarks = np.zeros([7, 3]).astype(np.float32)
#     with open(fname, 'r') as f:
#         lines = f.readlines()
#         for j in range(8, 15):
#             line_contentes = lines[j].split(' ')
#             # Check the .pp file to get to accurately pickup the columns for x , y and z coordinates
#             for i in range(len(line_contentes)):
#                 if line_contentes[i].split('=')[0] == 'x':
#                     x_content = float((line_contentes[i].split('=')[1]).split('"')[1])
#                 elif line_contentes[i].split('=')[0] == 'y':
#                     y_content = float((line_contentes[i].split('=')[1]).split('"')[1])
#                 elif line_contentes[i].split('=')[0] == 'z':
#                     z_content = float((line_contentes[i].split('=')[1]).split('"')[1])
#                 else:
#                     pass
#             lamdmarks[j - 8, :] = (np.array([x_content, y_content, z_content]).astype(np.float32))
#     return lamdmarks
#
#
# obj = bpy.context.object
# # landmarks = load_pp('/mnt/sata/data/NowDataset/NoW_Dataset/final_release_version/val_scanslmksonlypp/'
# #                     'scans_lmks_onlypp/FaMoS_180424_03335_TA/natural_head_rotation.000001_picked_points.pp')
# landmarks = np.load('/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBase/'
#                     'FaMoS_180424_03335_TA/multiview_expressions/IMG_0054.npy')
#
# print('\n\n\n\n\n')
# print(landmarks)
#
# for lnd in landmarks:
#     loc = obj.matrix_world @ mathutils.Vector((lnd))
#     bpy.ops.object.empty_add(type='PLAIN_AXES', location=loc)


#--------------- END ---------------#
import os
import subprocess
import glob
import numpy as np

root = '/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBaseNeutral'
objPaths = sorted(glob.glob(root + '/**/IMG*.obj', recursive=True))
blenderGenLmCoord = '/mnt/sata/code/myGit/3DFaceEvaluation/Now_Dataset/Blender/generateLandmarkCoords.py'
# objFilePath = '/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBase/' \
#               'FaMoS_180424_03335_TA/multiview_expressions/IMG_0053.obj'

for objpath in objPaths:
    if os.path.exists(objpath.replace('.obj','.npy')):
        continue
    # print(objpath)
    cmd = "blender --background -P " + blenderGenLmCoord + " -- " + objpath
    # print(cmd)
    # p = subprocess.call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
    p = subprocess.call(cmd, shell=True)


