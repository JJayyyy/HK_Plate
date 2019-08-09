#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""

@File: simplify_json.py
@License: Copyright (c) 2018-2019 Siemens, Inc.
@Author: Zhao Jie
@Time: 8/6/2019 9:50 AM
@Version: 1.0  
@Description: Remove the invalid annotations from the original json file.

"""

# import lib
import json
import argparse


def simplify_json(json_input, json_output):
    """
    Remove the invalid items from the original json file.
    To obtain a simplified .json version.
    :param json_input (file)
    :param json_output (file)
    :return: json_simplified (dict)
    """

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
    json_simplified = {}
    annotations = json.load(open(json_input))
    print("[INFO] Annotations without simplification: " + str(len(annotations)))

    for key, value in annotations.items():
        if value['regions']:
            json_simplified.update({key: value})
    print("[INFO] Annotations after simplification: " + str(len(json_simplified)))

    with open(json_output, 'w') as file_obj:
        json.dump(json_simplified, file_obj)
    print("[INFO] New json file is saved.")

    return json_simplified


if __name__ == '__main__':
    # Usage: python simplify_json.py -i /path/to/input_json.json -o /path/to/output_json.json
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, required=True,
                    help="path to input json file")
    ap.add_argument("-o", "--output", type=str, required=True,
                    help="path to output json file")
    args = vars(ap.parse_args())

    json_file = simplify_json(args["input"], args["output"])
    print("[INFO] Processing completed.")
