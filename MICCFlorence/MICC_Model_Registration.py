import glob
import os
import time
import numpy as np

import menpo3d.io as m3io
import menpo.io as mio
from menpo.shape import PointCloud
from menpo.transform import AlignmentSimilarity
from menpo3d.correspond import nicp
import argparse



def meshRegistration(source, template):
    # Simple Alignment
    lm_align = AlignmentSimilarity(source.landmarks['LJSON'], template.landmarks['LJSON']).as_non_alignment()
    source = lm_align.apply(source)

    # NICP registration
    result = nicp.non_rigid_icp(template, source, landmark_group='LJSON', verbose=True)
    return result


def main(args):
    MICC_path = args.MICC_path
    registration_path = args.save_path
    landmarks_only_path = args.landmarks

    template = m3io.import_mesh('../Data/MICCFlorence/BFM/bfm_model_front.obj')
    template_lms = np.array(mio.import_pickle('../Data/MICCFlorence/BFM/landmark_ids_bfm.pkl'))
    template.landmarks['LJSON'] = PointCloud(template.points[template_lms])

    dataset_paths = glob.glob(os.path.join(MICC_path, 'subject_*/Model/frontal*/obj/*.obj'))
    dataset_paths.sort()
    for source_path in dataset_paths:
        try:
            print('Processing: ' + source_path)
            start = time.time()

            export_path = source_path.replace(MICC_path, registration_path).replace('vrml', 'obj')
            _, extension = os.path.splitext(export_path)
            if not os.path.exists(os.path.dirname(export_path)):
                os.makedirs(os.path.dirname(export_path))

            if os.path.exists(export_path):
                if os.path.isfile(export_path):
                    print('Found, Skipping: ' + export_path)
                    continue
            print(source_path)
            source = m3io.import_mesh(source_path)
            source.landmarks['LJSON'] = \
            m3io.import_landmark_file(source_path.replace(MICC_path, landmarks_only_path).replace('.obj', '.ljson'))[
                'LJSON']

            result = meshRegistration(source, template)

            m3io.export_mesh(result, export_path)
            print('Took :' + '%.2f' % ((time.time() - start) / 60) + ' minutes')

        except Exception as e:
            print('Failed: ' + source_path)
            print(e)
            with open(os.path.join(registration_path, "logs.txt"), "a") as text_file:
                text_file.write('Failed: ' + source_path + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--MICC_path', default='Data/MICCFlorence/Reconstruction/GroundTruth',
                        help='Original directory of the MICC FLORENCE dataset')
    parser.add_argument('--save_path', default='Data/MICCFlorence/Reconstruction/BFMRegistered',
                        help='Path to save registration of the dataset')
    parser.add_argument('--landmarks', default='Data/MICCFlorence/MICC_landmarks',
                        help='Manually labelled ibug68 landmarks of the MICC dataset')
    args, other_args = parser.parse_known_args()
    main(args)
