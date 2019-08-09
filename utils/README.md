## Workflow & Steps

* simplify_json 
* rect_to_polygon
* obtain_images_from_json
* annotation_check
* open VIA, import images and json, check errors in last step

### simplify_json.py

Remove the invalid annotations from the original json file.

```
$ python simplify_json.py -i C:\path\to\input\json_file.json -o C:\path\to\output\new_json_file.json
```

### rect_to_polygon.py

Convert rect object to polygon object in json file.

```
$ python rect_to_polygon.py -i C:\path\to\input\json_file.json -o C:\path\to\output\new_json_file.json
```

### obtain_images_from_json.py

Pick the valid images from dataset.

```
$ python obtain_images_from_json.py -f C:\path\to\json_file.json -i C:\path\to\input_folder\ -o C:\path\to\output_folder\
```

### annotation_check.py

Check the annotations automatically for several mistakes. e.g. 1. No plate 2. Multiple plates 3. No label 4. No label selected

```
$ python annotation_check.py -i C:\path\to\json_file.json
```



