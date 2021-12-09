import glob
import os.path

import numpy as np

import menpo3d.io as m3io
import menpo.io as mio
from menpo.shape import PointCloud
from menpo.transform import AlignmentSimilarity
from menpo3d.correspond import nicp


def meshRegistration(templateObj, templateLandmarkPkl, sourceObj, sourceLandmarkLjson, exportPath):
    template = m3io.import_mesh(templateObj)
    template_lms = np.array(mio.import_pickle(templateLandmarkPkl))
    template.landmarks['LJSON'] = PointCloud(template.points[template_lms])

    source = m3io.import_mesh(sourceObj)
    source.landmarks['LJSON'] = m3io.import_landmark_file(sourceLandmarkLjson)['LJSON']

    lm_align = AlignmentSimilarity(source.landmarks['LJSON'], template.landmarks['LJSON']).as_non_alignment()
    source = lm_align.apply(source)
    # m3io.export_mesh(source, exportPath, overwrite=True)
    result = nicp.non_rigid_icp(template, source, landmark_group='LJSON', verbose=True)
    m3io.export_mesh(result, exportPath, overwrite=True)


templateObj = 'Data/MICCFlorence/BFM/bfm_model_front.obj'
templateLandmarkPkl = 'Data/MICCFlorence/BFM/landmark_ids_bfm.pkl'
sourceObjRoot = 'Data/MICCFlorence/Reconstruction/GroundTruth/'  # 110920150452.obj'
# sourceLandmarkLjson = 'Data/MICCFlorence/MICC_landmarks/subject_01/Model/frontal1/obj/110920150452.ljson'
exportPathRoot = 'Data/MICCFlorence/Reconstruction/BFMRegistered'
exportAlignedRoot = 'Data/MICCFlorence/Reconstruction/BFMAligned'

# meshRegistration(templateObj, templateLandmarkPkl, sourceObj, sourceLandmarkLjson, exportPath)


def main():
    for i in range(1, 54):
        sourceObj = None
        sourceLandmarkLjson = None
        exportPath = None
        # print(f"subject_{i:02d}")
        sourceObjPath = os.path.join(sourceObjRoot, f"subject_{i:02d}")
        sourceObjFile = glob.glob1(sourceObjPath, '*.obj')
        sourceObj = os.path.join(sourceObjPath, sourceObjFile[0])
        sourceLandmarks = glob.glob(f'Data/MICCFlorence/MICC_landmarks/subject_{i:02d}/**/*.ljson', recursive=True)
        for lnd in sourceLandmarks:
            if sourceObjFile[0].split('.')[0] == lnd.split('/')[-1].split('.')[0]:
                sourceLandmarkLjson = lnd
        exportPath = os.path.join(exportPathRoot, f"subject_{i:02d}", sourceObjFile[0])
        alignedPath = os.path.join(exportAlignedRoot, f"subject_{i:02d}", sourceObjFile[0])
        if None in [templateObj, templateLandmarkPkl, sourceObj, sourceLandmarkLjson, exportPath]:
            print('Issue :', sourceObjPath)
            continue
        print(exportPath)
        meshRegistration(templateObj, templateLandmarkPkl, sourceObj, sourceLandmarkLjson, exportPath)
        # meshRegistration(templateObj, templateLandmarkPkl, sourceObj, sourceLandmarkLjson, alignedPath)
        s = 1

# import open3d as o3d
# print(o3d)

# x = o3d.io.read_triangle_mesh('Test/110920150452.obj')
# bbox = o3d.geometry.AxisAlignedBoundingBox(min_bound=(-1, -1, -1), max_bound=(80000, 100000, 100000))
# y = x.crop(bbox)
# o3d.io.write_triangle_mesh('Test/1.obj', y)

# template = m3io.import_mesh('Data/MICCFlorence/BFM/bfm_model_front.obj')
# # template2 = m3io.import_mesh('template_ganfit_crop.obj')
#
# template_lms = np.array(mio.import_pickle('Data/MICCFlorence/BFM/landmark_ids_bfm.pkl'))
# # template_lms2 = np.array(mio.import_pickle('landmark_ids_ganfit_crop.pkl'))
#
# template.landmarks['LJSON'] = PointCloud(template.points[template_lms])
# # template2.landmarks['LJSON'] = PointCloud(template2.points[template_lms2])
#
#
# source = m3io.import_mesh('Data/MICCFlorence/Reconstruction/GroundTruth/subject_01/110920150452.obj')
# source.landmarks['LJSON'] = m3io.import_landmark_file('Data/MICCFlorence/MICC_landmarks/subject_01/Model/frontal1/obj/'
#                                                       '110920150452.ljson')['LJSON']
#
#
# lm_align = AlignmentSimilarity(source.landmarks['LJSON'], template.landmarks['LJSON']).as_non_alignment()
# source = lm_align.apply(source)
# # m3io.export_mesh(source, 'Test/bfm_aligned.obj')
#
# result = nicp.non_rigid_icp(template, source, landmark_group='LJSON', verbose=True)
# m3io.export_mesh(result, 'Data/Test/110920150452_reg.obj')
#
#
# s = 1

if __name__ == '__main__':
    main()
