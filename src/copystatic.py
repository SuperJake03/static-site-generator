import os
import shutil


def copy_directory(src, dst):
    items = os.listdir(src)
    for item in items:
        src_path = os.path.join(src, item)
        if os.path.isfile(src_path):
            print(f"***** COPYING {src_path} to {dst}")
            shutil.copy(src_path, dst)
        else:
            dst_path = os.path.join(dst, item)
            os.mkdir(dst_path)
            copy_directory(src_path, dst_path)


def copy_files_recursive(src, dst):
    if not os.path.exists(src):
        raise ValueError("Source directory does not exists")
    if os.path.exists(dst):
        print(f"***** DELETING {dst}")
        shutil.rmtree(dst)
    os.mkdir(dst)
    copy_directory(src, dst)
