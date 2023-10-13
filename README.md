# CD-Action Disc Centerer

A script for centering / leveling / straitening scans of CD-Action discs.

**This is most likely NOT the best solution (I've never worked with `cv2`) but it works and I imagine the resources bellow can also be pretty useful*

## TODO

- [ ] Cut out inner and outer circles
- [ ] Find common visual trait
- [ ] Find out rotation of trait
- [ ] Center the disc

- black edges on scan (put paper underneath?)
- speed issue (size - resolution and format?) -> fine tune scan export settings
- add instruction to `README.md` (venv + usage)
- investigate blur of the fin image?
- add example/s
- do repo
<!-- -->
- write article about this?

## Resources

### Manipulation

- [PIL - Reduce image file size](https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil)
- [OpenCV - Cropping an image](https://learnopencv.com/cropping-an-image-using-opencv/)
- [OpenCV - Image file reading and writing](https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html)

### Detection

- [OpenCV - Line detection](https://github.com/ClarityCoders/ZigZag/blob/master/lineDetection.py)
- [OpenCV - Edge detection](https://learnopencv.com/edge-detection-using-opencv/)
- [OpenCV - Object detection](https://www.youtube.com/watch?v=OzWU18AwS9k)
<!-- -->
- [Pytesseract - Basic bill detection system (OCR)](https://www.youtube.com/watch?v=qfO9gqqMWxU)
- [Pytesseract - Extract text from images in Python (OCR)](https://www.youtube.com/watch?v=PY_N1XdFp4w)

### Transforms

- [Desmos - Two point form](https://www.desmos.com/calculator/md6buy4efz?lang=pl)
- [Matura - Selected mathematical formulas](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/MATURA_2015_Wybrane_wzory_matematyczne.pdf)
<!-- -->
- [OpenCV - Hough line transform 1](https://docs.opencv.org/4.x/d6/d10/tutorial_py_houghlines.html)
- [OpenCV - Hough line transform 2](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html)
<!-- -->
- [OpenCV - Perspective transform from rotation angle](https://stackoverflow.com/questions/41428162/python-perspective-transform-for-opencv-from-a-rotation-angle)
- [OpenCV - Apply a transformation matrix to a list of points](https://stackoverflow.com/questions/43157092/applying-transformation-matrix-to-a-list-of-points-in-opencv-python)
<!-- -->
- [OpenCV - Rotation angle (`minAreaRect`)](https://theailearner.com/tag/opencv-rotation-angle/)
- [OpenCV - Determine angle of `RotatedRect` / `minAreaRect`](https://namkeenman.wordpress.com/2015/12/18/open-cv-determine-angle-of-rotatedrect-minarearect/)
- [OpenCV - The `getRotationMatrix2D()` function](https://www.geeksforgeeks.org/python-opencv-getrotationmatrix2d-function/)

### Repos

- [Image template matcher 1](https://github.com/brkyzdmr/TemplateMatcher)
- [Image template matcher 2](https://github.com/cozheyuanzhangde/Invariant-TemplateMatching)
