from PIL import Image, ImageDraw
import os
import argparse
from ia_common import *

description="""
    Draw line on image.
"""

def process_file(in_file, args):
    out_file = os.path.join(args.dst_folder, os.path.basename(in_file))
    print "%s ==> %s" % (in_file, out_file)
    
    im = Image.open(in_file).convert("RGB")
    draw = ImageDraw.Draw(im)
    draw.line(args.coords, width=args.width, fill=args.fill)
    del draw
    im.save(out_file)

def process_files(img_files, args):
    for f in img_files:
        process_file(f, args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("src_folder")
    parser.add_argument("dst_folder")
    parser.add_argument("--img_extension", default=".png")
    parser.add_argument("--width", default=3, type=int)
    parser.add_argument("--fill", default="888888")
    parser.add_argument("coords", nargs=4, type=int)
    args = parser.parse_args()
    
    process_files(get_list_of_image_files(args.src_folder, args.img_extension), args)
    