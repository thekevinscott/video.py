# video.py
# import os
import cv2
import sys
import pathlib
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('--source', help='The source file(s), separated by commas')
parser.add_argument('--target', help='The target directories, separated by commas')
parser.add_argument('--start', help='An optional argument to denote a starting frame.')
parser.add_argument('--end', help='An optional argument to denote an ending frame.')

args=parser.parse_args()

if not args.source:
    raise Exception('Please provide a source argument')
if not args.target:
    raise Exception('Please provide a target argument')

def separateFrames(source, target, start, end):
    pathlib.Path(target).mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start-1)
    success,image = cap.read()
    count = 0
    while success and (end is None or (end - start ) > count):
        fileTarget = "%s/%d.jpg" % (target, count)
        cv2.imwrite(fileTarget, image)
        success,image = cap.read()
        count += 1
        print('.')

source = args.source.split(',')
target = args.target.split(',')
start = 0 if args.start == '' else int(args.start)
end = None if args.end == '' else int(args.end)

if len(target) is not len(source):
    raise Exception('Mismatch between source and target args')

if (end is not None and end <= start):
    raise Exception('end argument must be greater than start argument')

for i, s in enumerate(source):
    separateFrames(s, target[i], start, end)
