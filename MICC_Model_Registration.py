import numpy as np

import menpo3d.io as m3io
import menpo.io as mio
from menpo.shape import PointCloud
from menpo.transform import AlignmentSimilarity
from menpo3d.correspond import nicp

# import open3d as o3d
# print(o3d)

# x = o3d.io.read_triangle_mesh('Test/110920150452.obj')
# bbox = o3d.geometry.AxisAlignedBoundingBox(min_bound=(-1, -1, -1), max_bound=(80000, 100000, 100000))
# y = x.crop(bbox)
# o3d.io.write_triangle_mesh('Test/1.obj', y)

template = m3io.import_mesh('Data/MICCFlorence/BFM/bfm_model_front.obj')
# template2 = m3io.import_mesh('template_ganfit_crop.obj')

template_lms = np.array(mio.import_pickle('Data/MICCFlorence/BFM/landmark_ids_bfm.pkl'))
# template_lms2 = np.array(mio.import_pickle('landmark_ids_ganfit_crop.pkl'))

template.landmarks['LJSON'] = PointCloud(template.points[template_lms])
# template2.landmarks['LJSON'] = PointCloud(template2.points[template_lms2])


source = m3io.import_mesh('Data/MICCFlorence/Reconstruction/GroundTruth/subject_01/110920150452.obj')
source.landmarks['LJSON'] = m3io.import_landmark_file('Data/MICCFlorence/MICC_landmarks/subject_01/Model/frontal1/obj/'
                                                      '110920150452.ljson')['LJSON']


lm_align = AlignmentSimilarity(source.landmarks['LJSON'], template.landmarks['LJSON']).as_non_alignment()
source = lm_align.apply(source)
# m3io.export_mesh(source, 'Test/bfm_aligned.obj')

result = nicp.non_rigid_icp(template, source, landmark_group='LJSON', verbose=True)
m3io.export_mesh(result, 'Data/Test/110920150452_reg.obj')


s = 1