# freeimage-py

Author: [Zachary Pincus](http://zplab.wustl.edu) <zpincus@gmail.com>

A Python module (compatible with both Python 2.7 and 3+) that provides image file IO to/from numpy arrays. Most common formats (notably PNG, TIFF and JPEG) are covered, along with a number of less-common formats. Reading and writing
single and multi-page images is supported, as well as many types of image metadata.

Images are read into numpy arrays of shape (x, y, c), where x is the image width, y is the height, and c is the number of color channels (3 for RGB and 4 for RGBA images). Greyscale images are shape (x, y). As is conventional, (0,0 refers to the top-left corner of the image. The images in memory are stored in the standard scanline format, and striding in numpy is used to present this format to the user in a straightforward (x, y, c) convention. Those more familiar with (y, x, c) C-style indexing into scanline images, or (c, x, y) Fortran-style indexing, can trivially convert to this convention with no memory copies by judicious use of the numpy.ndarray constructor with appropriately chosen shape and strides parameters.

This module provides an interface into a lightweight version of the [freeimage](http://freeimage.sourceforge.net) library. (RAW camera formats, WebP, JPEG-2000, JPEG-XR, and EXR support was removed to make building this module simpler. This support could easily be added back in by replacing the relevant source files from freeimage.) The freeimage library is built as a python extension so that there is no need for users to figure out how to build/obtain freeimage shared libraries on their platform; however the actual interface to the freeimage librariy is a set of ctypes wrappers that could be equally well used for an external libfreeimage if desired.

Freeimage itself is licensed under any of the three licenses provided in the Source directory (the Freeimage license, which is MIT-style, or GPL2 or 3); several sub-packages have separate licensing (MIT-style) specified therin. The  python code for freeimage-py is MIT licensed as well.