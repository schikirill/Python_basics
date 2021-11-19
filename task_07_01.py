import os

main_dir = 'my_project'
inner_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(main_dir):
    os.mkdir(main_dir)
[os.makedirs(os.path.join(main_dir, folder)) for folder in inner_dirs
 if not os.path.exists(os.path.join(main_dir, folder))]

with open('paths.txt', 'w') as f:
    f.writelines([main_dir, '\n'])
    [f.writelines([os.path.join(main_dir, folder), '\n']) for folder in inner_dirs]