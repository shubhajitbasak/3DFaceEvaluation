import os
import shutil
import glob

florenceImagePath = 'MICCFlorence/Images'
scenes = ['Indoor-Cooperative', 'PTZ-Indoor', 'PTZ-Outdoor']
florenceReconstructionPath = 'MICCFlorence/Reconstruction'


def createFlorenceImageFoleders():
    for i in range(1, 54):
        for scene in scenes:
            scenepath = os.path.join(florenceImagePath, f"subject_{i:02d}", scene)
            if not os.path.exists(scenepath):
                os.makedirs(scenepath, exist_ok=True)


def createFlorenceReconFolders():
    for folder in ['GroundTruth', 'BFMRegistered', 'BFMAligned']:
        for i in range(1, 54):
            reconPath = os.path.join(florenceReconstructionPath, folder, f"subject_{i:02d}")
            if not os.path.exists(reconPath):
                os.makedirs(reconPath, exist_ok=True)


def copyFlorenceGTData():
    MICCPath = '/mnt/sata/code/GANFit/data/MICC'
    GTPath = 'MICCFlorence/Reconstruction/GroundTruth'
    for i in range(1, 54):
        objFile = glob.glob(os.path.join(MICCPath, f"subject_{i:02d}", 'Model', 'frontal1', 'obj', '*.obj'))
        if len(objFile) > 0:
            # print(os.path.join(GTPath, f"subject_{i:02d}"))
            shutil.copyfile(objFile[0], os.path.join(GTPath, f"subject_{i:02d}", objFile[0].split('/')[-1]))
            # print(objFile[0], objFile[0].split('/')[-1])


def createImageListFile():
    imagePath = '/mnt/sata/code/myGit/3DFaceEvaluation/Data/MICCFlorence/Images'
    files = sorted(glob.glob(imagePath + '/**/*.jpg', recursive=True))
    test = 5


def movePredShapes():
    rawframePath = '/mnt/sata/data/Florence/FlorenceFace/RawFrames'
    targetFolder = 'Pred_Swin_Base'
    objfiles = sorted(glob.glob(rawframePath+ '/**/*.obj', recursive=True))
    for objfile in objfiles:
        newPath = os.path.dirname(objfile).replace('RawFrames', targetFolder)
        if not os.path.exists(newPath):
            os.makedirs(newPath, exist_ok=True)
        shutil.move(objfile, objfile.replace('RawFrames', targetFolder))


movePredShapes()
