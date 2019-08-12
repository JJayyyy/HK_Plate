## Workflow & Steps
* get the combined json file (e.g. 09-1.json 09-2.json 09-3.json → 09.json; Use notepad++ Json Viewer Plugin to combine)
* simplify_json.py 
* rect_to_polygon.py
* obtain_images_from_json.py
* annotation_check.py
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

### Open VIA, Import images and json, Check and correct errors in last step

### 多张车牌的情况，在VIA中把标注的内容全部删除即可

### 重复 Open VIA, Import images and json, Check and correct errors in last step直至所有错误都排除掉

### 导出json文件，运行一次simplify_json.py，去掉多张车牌的空标注；

### 得到最终json文件，上传git，将之前的文件替换


