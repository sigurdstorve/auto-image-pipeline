import argparse
import matplotlib.pyplot as plt
import os
from ia_common import *

description="""
    Semi-automatic image resizing tool.
"""

def process_file(in_file, args):
    out_file = os.path.join(args.dst_folder, os.path.basename(in_file))
    cmd = "convert %s -resize %sx%s %s" % (in_file, args.new_width, args.new_height, out_file)
    print "Executing: %s" % cmd
    os.system(cmd)
   
def process_files(file_list, args):
    for f in file_list:
        process_file(f, args)
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("src_folder", help="Source folder containing images [will not be modified]")
    parser.add_argument("dst_folder", help="Destination folder to put cropped images in")
    parser.add_argument("--new_width", help="New width in pixels", default="")
    parser.add_argument("--new_height", help="New height in pixels", default="")
    parser.add_argument("--img_extension", help=".png")
    args = parser.parse_args()
    if args.new_width == "" and args.new_height == "":
        print "Nothing to do"
        exit()
    process_files(get_list_of_image_files(args.src_folder, args.img_extension), args)
    