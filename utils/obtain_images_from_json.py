#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""

@File: obtain_images_from_json.py    
@License: Copyright (c) 2018-2019 Siemens, Inc.
@Author: Zhao Jie
@Time: 8/6/2019 9:52 AM
@Version: 1.0  
@Description: Pick the valid images from dataset.

"""

# import lib
import os
import json
import shutil
import pathlib
import argparse


def obtain_valid_images(json_file, src, dst):
    """
    Copy the valid images to the target folder.
    The paths of the valid images are recorded in .json file.
    :param json_file (file)
    :param src (folder)
    :param dst (folder)
    :return: list of images' paths
    """
    images_list = []
    # If the dst dir does not exist, then create
    pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    # Load annotations
    # VGG Image Annotator (up to version 2.0.8) saves each image in the form:
    # "2019-04-25-0d0c6d1e-5812-4375-af41-e539b88d06cd.jpg12872": {
    #     "filename": "2019-04-25-0d0c6d1e-5812-4375-af41-e539b88d06cd.jpg",
    #     "size": "12872",
    #     "regions": [
    #         {
    #             "shape_attributes": {
    #                 "name": "polygon",
    #                 "all_points_x": [...],
    #                 "all_points_y": [...]
    #             },
    #             "region_attributes": {
    #                 "class": "plate",
    #                 "view": "slantview",
    #                 "with_content": "No"
    #             }
    #         }
    #     ],
    #     "file_attributes": {}
    # },
    # We mostly care about the x and y coordinates of each region
    # Note: In VIA 2.0, regions was changed from a dict to a list.
    annotations = json.load(open(json_file))
    annotations = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images.
    annotations = [a for a in annotations if a['regions']]

    # Copy images from src folder to dst folder
    for a in annotations:
        image_path = os.path.join(src, a['filename'])
        try:
            shutil.copy2(image_path, os.path.join(dst, a['filename']))
            images_list.append(image_path)
        except BaseException as e:
            print("[ERROR] " + e + a['filename'])
    print("[INFO] Copy " + str(len(images_list)) + " images.")
    return images_list


if __name__ == '__main__':
    # Usage: python obtain_images_from_json.py -f /path/to/json_file.json -i /path/to/input_folder -o /path/to/output_folder
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", type=str, required=True,
                    help="path to json file")
    ap.add_argument("-i", "--input", type=str, required=True,
                    help="input image folder")
    ap.add_argument("-o", "--output", type=str, required=True,
                    help="output image folder")
    args = vars(ap.parse_args())
    valid_images = obtain_valid_images(args["file"], args["input"], args["output"])
    print("[INFO] Processing completed.")
