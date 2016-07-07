import argparse
import matplotlib.pyplot as plt
import os
from ia_common import *

description="""
    Semi-automatic image cropping tool.
    Works on files with the same name in two different folders.
"""

def process_file(in_file1, in_file2, args):
    basename1 = os.path.basename(in_file1)
    basename2 = os.path.basename(in_file2)
    #assert basename1 == basename2 # don't require equal extension...
    out_file = os.path.join(args.dst_folder, basename1)
    if args.mode == "horizontal":
        tile_str = "2x1"
    else:
        tile_str = "1x2"
    cmd = "montage -mode concatenate -tile %s %s %s %s" % (tile_str, in_file1, in_file2, out_file)
    print "Executing: %s" % cmd
    os.system(cmd)

def process_files(args):
    file_list1 = sorted(get_list_of_all_files(args.src_folder1))
    file_list2 = sorted(get_list_of_all_files(args.src_folder2))
    assert len(file_list1) == len(file_list2)
    for f1, f2 in zip(file_list1, file_list2):
        process_file(f1, f2, args)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("src_folder1", help="Source dir1 [will not be modified]")
    parser.add_argument("src_folder2", help="Source dir2 [will not be modified]")
    parser.add_argument("mode", choices=["horizontal", "vertical"])
    parser.add_argument("dst_folder", help="Destination dir")
    args = parser.parse_args()
    
    process_files(args)
    