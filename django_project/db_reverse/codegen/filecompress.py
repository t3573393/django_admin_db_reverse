#coding:utf8
import os
import zipfile
from django_project.settings import BASE_DIR


def zip_compress(dir_name, zip_file_target, path, exclude_files, target_path):
    if dir_name in exclude_files:
        return
    currentPath = "%s/%s" % (path, dir_name)
    if os.path.isdir(currentPath) == True:
        files = os.listdir(currentPath)
        for file in files:
            zip_compress(file, zip_file_target, currentPath, exclude_files, target_path +"/" + dir_name)
    else:
        zip_file_target.write(currentPath, target_path + "/" +dir_name)


def compress_in_folder():
    root_folder = BASE_DIR
    zipf = zipfile.ZipFile('%s/result.zip' % root_folder, 'w')
    # zip the path
    dir_path = '%s/db_reverse/temp' % root_folder
    files = os.listdir(dir_path)
    exclude_file = []
    for file in files:
        if file not in exclude_file:
            zip_compress(file, zipf, dir_path, exclude_file, "")
    zipf.close()


def save_string_to_file(file_name, content):
    print BASE_DIR
    root_folder = BASE_DIR
    temp_file = '%s/db_reverse/temp/%s' % (root_folder, file_name)
    fh = open(temp_file, 'w+')
    fh.write(content)
    fh.close()