import numpy as np
import PIL
import os

def load_image_as_numpy_array(img_file):
    return np.array(PIL.Image.open(img_file))

def get_image_dimensions(img_file):
    """ return width, height """
    shape = load_image_as_numpy_array(img_file).shape
    width = shape[1]
    height = shape[0]
    return width, height

def get_list_of_image_files(root_dir, img_extension):
    res = []
    for f in os.listdir(root_dir):
        if os.path.splitext(f)[1] == img_extension:
            res.append(os.path.join(root_dir, f))
    return res

def get_list_of_all_files(root_dir):
    return map(lambda basename: os.path.join(root_dir, basename), os.listdir(root_dir))

def equal_file_lists(l1, l2):
    for f1 in l1:
        if not f1 in l2: return False
    for f2 in l2:
        if not f2 in l1: return False
    return True
    