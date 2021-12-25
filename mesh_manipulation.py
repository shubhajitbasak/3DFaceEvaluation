import numpy as np
import menpo3d.io as m3io
import menpo.io as mio
from menpo.shape import PointCloud

template = m3io.import_mesh('/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBase/'
                            'FaMoS_180424_03335_TA/multiview_expressions/IMG_0053.obj')
template_lms = np.array(mio.import_pickle('Data/MICCFlorence/BFM/landmark_ids_bfm.pkl'))
template.landmarks['LJSON'] = PointCloud(template.points[template_lms])
print('tst')
