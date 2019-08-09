#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""

@File: rect_to_polygon.py    
@License: Copyright (c) 2018-2019 Siemens, Inc.
@Author: Zhao Jie
@Time: 8/7/2019 8:43 PM
@Version: 1.0  
@Description: Convert rect to polygon in json file

"""

# import lib
import json
import argparse


def rect_to_polygon(json_input, json_output):
    """
    Convert rect object to polygon object in json file.
    :param json_input:
    :param json_output:
    :return:
    """
    rect_count = 0
    annotations = json.load(open(json_input))
    for key, value in annotations.items():
        if value['regions']:
            for r in value['regions']:
                if r['shape_attributes']['name'] == 'rect':
                    rect_count = rect_count + 1
                    x = r['shape_attributes']['x']
                    y = r['shape_attributes']['y']
                    width = r['shape_attributes']['width']
                    height = r['shape_attributes']['height']
                    all_points_x = [x, x + width, x + width, x]
                    all_points_y = [y, y, y + height, y + height]
                    r['shape_attributes']['all_points_x'] = all_points_x
                    r['shape_attributes']['all_points_y'] = all_points_y
                    # Remove x, y, width, height
                    r['shape_attributes'].pop('x')
                    r['shape_attributes'].pop('y')
                    r['shape_attributes'].pop('width')
                    r['shape_attributes'].pop('height')
                    r['shape_attributes']['name'] = 'polygon'
    print("[INFO] Convert " + str(rect_count) + " Rect object to Polygon.")
    with open(json_output, 'w') as file_obj:
        json.dump(annotations, file_obj)

    return annotations


if __name__ == '__main__':
    # Usage: python rect_to_polygon.py -i /path/to/input_json.json -o /path/to/output_json.json
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, required=True,
                    help="path to input json file")
    ap.add_argument("-o", "--output", type=str, required=True,
                    help="path to output json file")
    args = vars(ap.parse_args())
    rect_to_polygon(args["input"], args["output"])
    print("[INFO] Processing completed.")
