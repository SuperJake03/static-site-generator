import os
import shutil

from copystatic import copy_files_recursive
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    copy_files_recursive(dir_path_static, dir_path_public)


main()
