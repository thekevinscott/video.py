import cv2
import os
import os.path
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('--source', help='The source file(s), separated by commas')
parser.add_argument('--target', help='The target directories, separated by commas')

args=parser.parse_args()

if not args.source:
    raise Exception('Please provide a source argument')
if not args.target:
    raise Exception('Please provide a target argument')

def separateFrames(source, target):
    print('sep 1')
    os.makedirs(target, exist_ok=True)
    print('sep 2')
    cap = cv2.VideoCapture(source)
    success,image = cap.read()
    print(success, image)
    if success is False:
        raise Exception('Could not read video file')

    count = 0
    while success:
        fileTarget = "%s/%d.jpg" % (target, count)
        # fileTarget = "%d.jpg" % (count)
        # fileTarget = os.path.join('/pfs/out', os.path("%d.jpg" % (count)))
        print('file target', fileTarget)
        cv2.imwrite(fileTarget, image)
        success,image = cap.read()
        count += 1
        print('.', end='')

source = args.source.split(',')
target = args.target.split(',')

if len(target) is not len(source):
    raise Exception('Mismatch between source and target args')

for i, s in enumerate(source):
    file = source[i]
    # file = os.path.join('/pfs/videos', source[i])
    separateFrames(file, target[i])


