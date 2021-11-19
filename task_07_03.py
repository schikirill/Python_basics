import os
import shutil

with open('paths_03.txt', 'r') as f:
    for row in f.read().splitlines():
        if not os.path.exists(row) and not row.lower().__contains__('.'):
            os.mkdir(row)
        elif row.lower().__contains__('.'):
            with open(row, 'w') as new_file:
                new_file.write("")

upper_dir = 'my_project'
dst_dir = 'my_project/templates'
for dir_path, dir_names, file_names in os.walk(upper_dir):
    if dir_path.split('\\')[-1] == 'templates':
        for dirs in dir_names:
            src = os.path.join(dir_path, dirs)
            dst = os.path.join(dst_dir, dirs)
            if not os.path.exists(dst):
                shutil.copytree(src, dst)