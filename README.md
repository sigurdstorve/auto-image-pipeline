# auto-image-pipeline
Utility scripts on top of PIL and ImageMagick for automating combinations of crop,resize,combine, and draw.

Operates on folders containing images. The following are supported:
- Crop images
- Resize to target width or height
- Combine two images either horizontally or vertically
- Annotate image by drawing lines.

Very useful to make animations from multiple image sequences with frames that correspond to each other. By chaining together the four supported operations, complex transformation hierarchies can easily be realized.

Currently each transformation is done on ALL images step-by-step, which potentially requires a lot of temporary disk space. A straightforward extension would be to do the entire processing chain on one frame at the time.
