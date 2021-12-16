import json
import numpy as np

with open('../../Test/110920150452.ljson') as f1:
    data = json.load(f1)

# s = data['groups']['LJSON']['landmarks']['points']

# loc = np.load('landmark_ids_loc.npy').tolist()

data['groups']['LJSON']['landmarks']['points'] = np.load('landmark_ids_loc.npy').tolist()

with open('../../Test/landmark_ids_bfm.ljson', 'w') as f2:
    json.dump(data, f2, indent=4)

# import menpo3d.io as m3io
# import menpo.io as mio
# from menpo.shape import PointCloud
# from menpo.transform import AlignmentSimilarity
# from menpo3d.correspond import nicp
#
# templateObj = '../../Test/bfm_model_front.obj'
# templateLandmarkPkl = '../../Test/landmark_ids_bfm.pkl'
# templateLandmarkLjson = '../../Test/landmark_ids_bfm.ljson'
# sourceObj = '../../Test/110920150452.obj'
# sourceLandmarkLjson = '../../Test/110920150452.ljson'
# exportPath = '../../Test/110920150452_reg.obj'
#
# template = m3io.import_mesh(templateObj)
# # template_lms = np.array(mio.import_pickle(templateLandmarkPkl))
# # template.landmarks['LJSON'] = PointCloud(template.points[template_lms])
# template.landmarks['LJSON'] = m3io.import_landmark_file(templateLandmarkLjson)['LJSON']
#
# source = m3io.import_mesh(sourceObj)
# source.landmarks['LJSON'] = m3io.import_landmark_file(sourceLandmarkLjson)['LJSON']
#
# lm_align = AlignmentSimilarity(source.landmarks['LJSON'], template.landmarks['LJSON']).as_non_alignment()
# source = lm_align.apply(source)
# # m3io.export_mesh(source, 'Test/bfm_aligned.obj')
# result = nicp.non_rigid_icp(template, source, landmark_group='LJSON', verbose=True)
# m3io.export_mesh(result, exportPath, overwrite=True)


