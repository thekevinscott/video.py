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
    os.makedirs(target, exist_ok=True)
    cap = cv2.VideoCapture(source)
    success,image = cap.read()
    if success is False:
        raise Exception('Could not read video file')

    count = 0
    while success:
        fileTarget = "%s/%d.jpg" % (target, count)
        cv2.imwrite(fileTarget, image)
        success,image = cap.read()
        count += 1
        print('.', end='')

source = args.source.split(',')
target = args.target.split(',')

if len(target) is not len(source):
    raise Exception('Mismatch between source and target args')

for i, file in enumerate(source):
    separateFrames(file, target[i])
