#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description='Generate micromouse maze text data from pictures.')

    # if '--classic' is specified, generate classic maze (maze size is 16x16)
    # currently only classic maze is tested
    parser.add_argument('--classic', action='store_true', help='Generate classic maze', default=True)

    parser.add_argument('picture', type=str, help='Input picture filename (bmp, png, jpg)')
    return parser.parse_args()


def get_average_intensity(image, x, y, size=6):
    half_size = size // 2
    region = image[y-half_size:y+half_size, x-half_size:x+half_size]

    mean_intensity = np.mean(region)

    return mean_intensity

def main():
    args = get_args()
    src = cv2.imread(args.picture, cv2.IMREAD_GRAYSCALE)
    src = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

    # resize to 640x640 pixels
    pixels = 640
    src = cv2.resize(src, (pixels, pixels))

    size = 16 if args.classic else 32

    # print the maze
    print("+" + "-+" * size)


    step = pixels // size
    offset = step // 2

    vert = []
    for j in range(size):
        line = "|"
        for i in range(size-1):
#            cv2.drawMarker(src, tuple([(i+1)*step, j*step+offset]), (255, 0, 0), thickness=1)
            intensity = get_average_intensity(src, (i+1)*step, j*step+offset)
#            print(intensity, end=' ')
            if i == 7 and j == 7:
                line += ("G|" if intensity > 15 else "G ")
            else:
                line += (" |" if intensity > 15 else "  ")
        vert.append(line + " |")

    hori = []
    for j in range(size-1):
        line = "+"
        for i in range(size):
#            cv2.drawMarker(src, tuple([i*step+offset, (j+1)*step]), (0, 255, 0), thickness=1)
            intensity = get_average_intensity(src, i*step+offset, (j+1)*step)
#            print(intensity, end=' ')
            line += ("-+" if intensity > 15 else " +")
        hori.append(line)
    hori.append("+" + "-+" * size)

    for j in range(size):
        print(vert[j])
        print(hori[j])

#    cv2.imshow('src', src)
#    cv2.waitKey(0)

if __name__ == '__main__':
    main()