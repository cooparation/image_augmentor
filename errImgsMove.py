import os
import cv2
from collections import OrderedDict

paths = ['trainSets']
file_type_list =['GIF', 'gif', 'jpeg',  'bmp', 'png', 'JPG',  'jpg', 'JPEG']
#file_type_list = ['jpg']

for path in paths:
    for root, _, files in os.walk(path):
        for filename in files:
            images = str(os.path.join(root, filename))
            #if "__trans" in images:
            if "__noise" in images:
                print "rm images: ", images
                os.remove(images)
            if "__trans" in images:
                print "rm images: ", images
                os.remove(images)
            if "__blur" in images:
                print "rm images: ", images
                os.remove(images)
