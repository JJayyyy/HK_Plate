#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""

@File: annotation_check.py
@License: Copyright (c) 2018-2019 Siemens, Inc.
@Author: Zhao Jie
@Time: 8/7/2019 2:59 PM
@Version: 1.0  
@Description: Check the annotations automatically for several mistakes.
              e.g. 1. No plate 2. Multiple plates 3. No class label

"""

# import lib
import json
import argparse


def annotation_check(json_file):
    """
    Check the annotations automatically for several mistakes. e.g. 1. No plate 2. Multiple plates 3. No label 4. No label selected
    :param json_file: annotation json file
    :return:
    """

    # Load annotations
    # VGG Image Annotator (up to version 1.6) saves each image in the form:
    # { 'filename': '28503151_5b5b7ec140_b.jpg',
    #   'regions': {
    #       '0': {
    #           'region_attributes': {},
    #           'shape_attributes': {
    #               'all_points_x': [...],
    #               'all_points_y': [...],
    #               'name': 'polygon'}},
    #       ... more regions ...
    #   },
    #   'size': 100202
    # }
    # We mostly care about the x and y coordinates of each region
    # Note: In VIA 2.0, regions was changed from a dict to a list.
    annotations = json.load(open(json_file))
    annotations = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images. => Get the list of valid annotations
    annotations = [a for a in annotations if a['regions']]

    # Add images
    for a in annotations:
        # Get the x, y coordinaets of points of the polygons that make up
        # the outline of each object instance. These are stores in the
        # shape_attributes (see json format above)

        # To count the number of plate in one picture
        plate_count = 0

        # [regions] is list type for version 2.x
        for r in a['regions']:
            try:
                class_name = r['region_attributes']['class']
                if len(class_name) == 0:
                    print("[ERROR] Empty class name: " + a['filename'])
                elif r['region_attributes']['class'] == "plate":
                    plate_count = plate_count + 1
            except BaseException as e:
                print("[ERROR] Key error of " + str(e) + ": " + a['filename'])

        if plate_count == 0:
            print("[ERROR] No plate in picture: " + a['filename'])
        elif plate_count > 1:
            print("[ERROR] Multiple plates in picture: " + a['filename'])


if __name__ == '__main__':
    # Usage: python annotation_check.py -i /path/to/input.json
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, required=True,
                    help="path to json file")
    args = vars(ap.parse_args())
    annotation_check(args["input"])
    print("[INFO] Processing completed.")
