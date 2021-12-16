import cv2
import mediapipe as mp
import glob
import os
import shutil
# from facenet_pytorch import MTCNN
# from PIL import Image
# from matplotlib import pyplot as plt
import numpy as np


def midpoint(p1, p2):
    coords = (p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0
    return coords


def relative_coord(shape, coord):
    x = coord[0]
    y = coord[1]
    relative_x = round(x * shape[1], 2)
    relative_y = round(y * shape[0], 2)
    return relative_x, relative_y


def generate5keypoints(img):
    mp_face_mesh = mp.solutions.face_mesh
    with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.9) as face_mesh:
        # annotated_image = image.copy()
        results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if results.multi_face_landmarks is None or len(results.multi_face_landmarks) > 1:
            return None
        else:

            for face in results.multi_face_landmarks:
                shape = img.shape

                leftEye = relative_coord(shape, midpoint(face.landmark[33], face.landmark[133]))
                rightEye = relative_coord(shape, midpoint(face.landmark[362], face.landmark[263]))
                noseTip = relative_coord(shape, (face.landmark[1].x, face.landmark[1].y))
                mouthLeft = relative_coord(shape, (face.landmark[57].x, face.landmark[57].y))
                mouthRight = relative_coord(shape, (face.landmark[287].x, face.landmark[287].y))

                features = [leftEye, rightEye, noseTip, mouthLeft, mouthRight]
                return features


def main():
    imagepath = '/mnt/sata/data/Florence/FlorenceFace/RawFrames/'
    imagefiles = sorted(glob.glob(imagepath + '/**/*.jpg', recursive=True))
    # filelist = []
    for img in imagefiles:
        image = cv2.imread(img)
        detectionPath = img.replace('.jpg', '.txt')
        if os.path.exists(detectionPath):
            os.remove(detectionPath)
        lndmrks = generate5keypoints(image)
        if lndmrks is not None:
            with open(detectionPath, "a") as f:  # img_addr.split('.')[0] + ".txt"
                for i in lndmrks:
                    print(str(i[0]) + ' ' + str(i[1]), file=f)
            # filelist.append(img + ',' + detectionPath)
        else:
            print('Issue : ', img)
            os.remove(img)

    # if os.path.exists('Data/MICCFlorence/Images/imagelist.txt'):
    #     os.remove('Data/MICCFlorence/Images/imagelist.txt')
    # with open('Data/MICCFlorence/Images/imagelist.txt', 'a+') as f1:
    #     for file in filelist:
    #         f1.write(file + '\n')


# draw the bounding boxes for face detection
def draw_bbox(bounding_boxes, image):
    for i in range(len(bounding_boxes)):
        x1, y1, x2, y2 = bounding_boxes[i]
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)),
                      (0, 0, 255), 2)

    return image


# plot the facial landmarks
def plot_landmarks(landmarks, image):
    for i in range(len(landmarks)):
        for p in range(landmarks[i].shape[0]):
            cv2.circle(image,
                      (int(landmarks[i][p, 0]), int(landmarks[i][p, 1])),
                      2, (0, 0, 255), -1, cv2.LINE_AA)
    return image


def cleanMICCFaceImage(root):
    mtcnn = MTCNN(margin=10, select_largest=True, post_process=False, device='cuda:0')

    imagefiles = sorted(glob.glob(root + '/**/*.jpg', recursive=True))

    for impath in imagefiles:

        try:
            frame = Image.open(impath)
            boxes, probs, _ = mtcnn.detect(frame, landmarks=True)
            if probs[0] is None or probs[0] < 0.99:
                print(impath, '  :  ', probs)
                os.remove(impath)
            elif boxes[0][3] > frame.height:
                print(impath)
                os.remove(impath)
            elif boxes[0][2] > frame.width:
                print(impath)
                os.remove(impath)
            elif boxes[0][0] < 0:
                print(impath)
                os.remove(impath)
        except:
            print(impath)
            os.remove(impath)


def displayfilecount(root):
    scene = ['Indoor-Cooperative', 'PTZ-Indoor', 'PTZ-Outdoor']
    for sub in next(os.walk(root))[1]:
        for scn in scene:
            print(os.path.join(root, sub, scn))
            print(len(glob.glob1(os.path.join(root, sub, scn),'*.jpg')))

    # for scn in scene:


if __name__ == '__main__':
    # main()
    # cleanMICCFaceImage('/mnt/sata/data/Florence/FlorenceFace/RawFrames/subject_2*')
    displayfilecount('/mnt/sata/data/Florence/FlorenceFace/RawFrames')

    # imagepath = '/mnt/sata/data/Florence/FlorenceFace/RawFrames'
    # videofiles = sorted(glob.glob(imagepath + '/**/*.obj', recursive=True))
    #
    # for f in videofiles:
    #     # os.remove(f)
    #     os.makedirs(os.path.dirname(f.replace('RawFrames', 'Pred_Microsoft3d')), exist_ok=True)
    #     shutil.move(f, f.replace('RawFrames', 'Pred_Microsoft3d'))






