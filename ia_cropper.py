import argparse
import matplotlib.pyplot as plt
import os
from ia_common import *

description="""
    Semi-automatic image cropping tool.
"""

def process_file(in_file, args):
    out_file = os.path.join(args.dst_folder, os.path.basename(in_file))
    cmd = "convert -crop %s %s %s" % (args.crop_region_str, in_file, out_file)
    print "Executing: %s" % cmd
    os.system(cmd)

def process_files(file_list, args):
    for f in file_list:
        process_file(f, args)
            
def get_crop_region_str(img):
    width, height = get_image_dimensions(img)
    im = load_image_as_numpy_array(img)
    plt.figure()
    plt.imshow(im, aspect="auto", interpolation="nearest")
    plt.title("Click top-left, then bottom-right")
    top_left, bottom_right = plt.ginput(2)
    width = int(bottom_right[0]-top_left[0])
    height = int(bottom_right[1]-top_left[1])
    return "%dx%d+%d+%d" % (width, height, top_left[0], top_left[1])
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("src_folder", help="Source folder containing images [will not be modified]")
    parser.add_argument("dst_folder", help="Destination folder to put cropped images in")
    parser.add_argument("--img_extension", help=".png")
    parser.add_argument("--crop_region_str", help="ImageMagick crop description [for fully automatic operation]", default="")
    args = parser.parse_args()
    
    file_list = get_list_of_image_files(args.src_folder, args.img_extension)
    assert len(file_list) > 0
    if args.crop_region_str == "":
        # get it by manually clicking
        args.crop_region_str = get_crop_region_str(file_list[0])
    process_files(file_list, args)
