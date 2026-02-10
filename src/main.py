import os
import shutil
import sys

from copystatic import copy_files_recursive
from generate_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_content = "./content"
dir_path_template = "./template.html"
dir_path_docs = "./docs"


def main():
    basepath = sys.argv[1] if sys.argv[1] != "" else "/"
    copy_files_recursive(dir_path_static, dir_path_docs)
    generate_pages_recursive(
        basepath, dir_path_content, dir_path_template, dir_path_docs
    )


main()
