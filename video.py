# video.py
# import os
import cv2
import sys
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
    print(source)
    print(target)
    vidcap = cv2.VideoCapture(source)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

source = args.source.split(',')
target = args.target.split(',')

if len(target) is not len(source):
    raise Exception('Mismatch between source and target args')

for i, s in enumerate(source):
    separateFrames(s, target[i])
