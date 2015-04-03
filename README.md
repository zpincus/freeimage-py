# freeimage-py

Author: Zachary Pincus <zpincus@gmail.com>

A Python module (compatible with both Python 2.7 and 3+) that provides image file IO to/from numpy arrays. Most common formats (notably PNG, TIFF and JPEG) are covered, along with a number of less-common formats.

This module provides an interface into a lightweight version of the [freeimage](http://freeimage.sourceforge.net) library. (RAW camera formats, WebP, JPEG-2000, JPEG-XR, and EXR support was removed to make building this module simpler. This support could easily be added back in by replacing the relevant source files from freeimage.) The freeimage library is built as a python extension so that there is no need for users to figure out how to build/obtain freeimage shared libraries on their platform; however the actual interface to the freeimage librariy is a set of ctypes wrappers that could be equally well used for an external libfreeimage if desired.


