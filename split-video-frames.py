import cv2
import os
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
    print('separate frames')
    # os.mkdir(target)
    cap = cv2.VideoCapture(source)
    print('got cap')
    cap.set(cv2.CAP_PROP_POS_FRAMES, start-1)
    print('cap set')
    success,image = cap.read()
    print(success, image)
    count = 0
    while success and (end is None or (end - start) > count):
        print('while still true', count)
        # fileTarget = "%s/%d.jpg" % (target, count)
        fileTarget = "%d.jpg" % (count)
        print('file target', fileTarget)
        cv2.imwrite(fileTarget, image)
        print('written')
        success,image = cap.read()
        print(success, image)
        count += 1
        print('.')
        print('.', end='')

source = args.source.split(',')
target = args.target.split(',')
start = 0 if not args.start else int(args.start)
end = None if not args.end else int(args.end)

if len(target) is not len(source):
    raise Exception('Mismatch between source and target args')

if (end is not None and end <= start):
    raise Exception('end argument must be greater than start argument')

for i, s in enumerate(source):
    print('source', source)
    separateFrames(s, target[i], start, end)
