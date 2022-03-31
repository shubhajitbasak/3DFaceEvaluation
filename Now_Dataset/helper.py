import numpy as np
import os

# t1 = np.load(
#     '/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBaseNeutral/FaMoS_180424_03335_TA/'
#     'multiview_expressions/IMG_0053.npy')
# t2 = np.load(
#     '/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBaseNeutral/FaMoS_180424_03335_TA/'
#     'multiview_expressions/IMG_0054.npy')
# print(t1)
#
# print('\n\n\n')
# print(t2)

# from official github


def load_pp(fname):
    lamdmarks = np.zeros([7, 3]).astype(np.float32)
    with open(fname, 'r') as f:
        lines = f.readlines()
        for j in range(8, 15):
            line_contentes = lines[j].split(' ')
            # Check the .pp file to get to accurately pickup the columns for x , y and z coordinates
            for i in range(len(line_contentes)):
                if line_contentes[i].split('=')[0] == 'x':
                    x_content = float((line_contentes[i].split('=')[1]).split('"')[1])
                elif line_contentes[i].split('=')[0] == 'y':
                    y_content = float((line_contentes[i].split('=')[1]).split('"')[1])
                elif line_contentes[i].split('=')[0] == 'z':
                    z_content = float((line_contentes[i].split('=')[1]).split('"')[1])
                else:
                    pass
            lamdmarks[j - 8, :] = (np.array([x_content, y_content, z_content]).astype(np.float32))
    return lamdmarks


# t3 = load_pp('/mnt/sata/data/NowDataset/NoW_Dataset/final_release_version/val_scanslmksonlypp/scans_lmks_onlypp/'
#              'FaMoS_180424_03335_TA/natural_head_rotation.000001_picked_points.pp')
#
# print(t3)

# t4 = np.load('/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBaseNeutral/results/_computed_distances.npy', allow_pickle=True)

# l = []
# for row in t4:
#     l.append(np.mean(row))

# print(t4)
# print(t4.shape)


with open('/mnt/sata/data/NowDataset/NoW_Dataset/final_release_version/imagepathstest.txt', mode='r') as f :
    files = f.readlines()

for f in files:
    objpath = os.path.join('/mnt/sata/data/NowDataset/NoW_Dataset/ModelOutput/SwinBaseNeutral', f.strip()).replace('jpg','obj')
    if not os.path.exists(objpath):
        print(objpath)
        print(os.path.join('/mnt/sata/data/NowDataset/NoW_Dataset/final_release_version/iphone_pictures', f.strip()))

