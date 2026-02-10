import os
import shutil
import sys

from copystatic import copy_files_recursive
from generate_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_content = "./content"
dir_path_template = "./template.html"
dir_path_docs = "./docs"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1 and sys.argv[1] != "":
        basepath = sys.argv[1] + "/"
    copy_files_recursive(dir_path_static, dir_path_docs)
    generate_pages_recursive(
        basepath, dir_path_content, dir_path_template, dir_path_docs
    )


main()
