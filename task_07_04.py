import os

directory = r'.'        """тут можно сделать запрос на ввод нужной папки, но без диалогового окна лень писать руками"""
files_size = {}
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)
        dict_keys = (10 ** len(str(size)))
        if dict_keys in files_size:
            files_size[dict_keys] += 1
        else:
            files_size[dict_keys] = 1

keys = list(files_size)
keys.sort()
for dict_keys in keys:
    print(f'{dict_keys}: {files_size[dict_keys]}')