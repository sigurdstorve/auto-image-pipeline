::Example: How to use
::INPUT FOLDERS WITH IMAGES:
::      FramesA/
::      FramesB/
::      FramesC/
::The result will be in the folder FINAL. 

python ia_line_drawer.py FramesA FramesA_WITH_LINE 383 0 383 799 --img_extension .bmp --width 5 --fill #666600
python ia_cropper.py FramesB FramesB_CROPPED --img_extension .bmp --crop_region_str 294x358+62+298
python ia_cropper.py FramesA_WITH_LINE FramesA_CROPPED --img_extension .bmp --crop_region_str 552x543+123+247
python ia_resizer.py FramesB_CROPPED FramesB_CROPPED_RESIZED --img_extension .bmp --new_height 543
python ia_combiner.py FramesB_CROPPED_RESIZED FramesA_CROPPED horizontal combined_horizontal
python ia_cropper.py FramesC FramesC_CROPPED --img_extension .png --crop_region_str 1389x316+228+41
python ia_resizer.py FramesC_CROPPED FramesC_CROPPED_RESIZED --img_extension .png --new_width 998
python ia_combiner.py combined_horizontal FramesC_CROPPED_RESIZED vertical FINAL
