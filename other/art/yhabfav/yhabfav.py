# import statements
import face_recognition as fr
from PIL import Image, ImageDraw
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
gr = 1.618 # define the golden ratio for error testing
# load image
img = fr.load_image_file("img.png")
f_locations = fr.face_locations(img)

# generate landmakrs
f_ll = fr.face_landmarks(img)

# create pil image
pil_image = Image.fromarray(img)
d = ImageDraw.Draw(pil_image)

# print landmarks and draw locations
for landmark in f_ll:
    # Print the location of each facial feature in this image
    for feature in landmark.keys():
        print("The {} in this face has the following points: {}".format(
            feature, landmark[feature]))
    # d.line takes in the list of points to draw as x,y coor tuples as
    # well as the width of the line to draw
    for feature in landmark.keys():
        d.line(landmark[feature], width=5)

# Extract Data
chin = landmark['chin']
nose_tip = landmark['nose_tip']
nose_bridge = landmark['nose_bridge']
left_eye = landmark['left_eye']
right_eye = landmark['right_eye']
left_eyebrow = landmark['left_eyebrow']
right_eyebrow = landmark['right_eyebrow']
top_lip = landmark['top_lip']
bottom_lip = landmark['bottom_lip']

# show current output
pil_image.show()

# Given the set of data points which outline Ainas gorgeous features
# define axes of symmetry around an ellipse with semi major axis from 
# nose to lower chin, and semi minor axis from nose to ear edges
def axes_of_sym(nose_tip, chin, nose_bridge):
    # define the major axis to be that of the average of the nose_bridge
    # extract x data and y data
    bxdata = []
    bydata = []
    txdata = []
    tydata = []
    for coors in nose_bridge:
        bxdata.append(coors[0])
        bydata.append(coors[1])
    for coors in nose_tip:
        txdata.append(coors[0])
        tydata.append(coors[1])
    bxdata = np.array(bxdata)
    bydata = np.array(bydata)
    txdata = np.array(txdata)
    tydata = np.array(tydata)
    # run polyfitting
    major = (np.average(bxdata), np.average(bydata))
    minor = (np.average(txdata), np.average(tydata))
    return major, minor
# given the set of data for the left eye, determine the curvature, relate
# to the golden ratio, compare to the right eye, and displacement from 
# semi major axis
def eyes(left_eye, right_eye, axis_xcenter):
    # take the centers of the left and right eye, find their displacement
    # from the center of the major axis. Also identify the xy coors of 
    # minx, miny to maxx, maxy to draw boxes to calculaute the golden
    # ratio
    lexdata = []
    leydata = []
    rexdata = []
    reydata = []
    for coors in left_eye:
        lexdata.append(coors[0])
        leydata.append(coors[1])
    for coors in right_eye:
        rexdata.append(coors[0])
        reydata.append(coors[1])
    lexdata = np.array(lexdata)
    leydata = np.array(leydata)
    rexdata = np.array(rexdata)
    reydata = np.array(reydata)
    # find the corners
    lexmin = min(lexdata)
    lexmax = max(lexdata)
    leymin = min(leydata)
    leymax = max(leydata)
    rexmin = min(rexdata)
    rexmax = max(rexdata)
    reymin = min(reydata)
    reymax = max(reydata)
    # find x displacement from major axis
    lexcenter = np.average(lexdata)
    rexcenter = np.average(lexdata)
    ledis = np.abs(lexcenter - axis_xcenter)
    redis = np.abs(rexcenter - axis_xcenter)
    dis_ratio = ledis/redis
    # determine areas
    lewidth = lexmax-lexmin
    leheight = leymax-leymin
    rewidth = rexmax-rexmin
    reheight = reymax-reymin
    learea = (lewidth)*(leheight)
    rearea = (rewidth)*(reheight)
    area_ratio = learea/rearea
    # compare width and height
    leratio = ledis/lewidth
    reratio = redis/rewidth
    leratio_offset = (leratio - gr)/gr
    reratio_offset = (reratio - gr)/gr
    # return values
    return [dis_ratio, area_ratio, leratio_offset, reratio_offset]
# given the set of data for the top and bottom lip, compare their
# respective areas, as well as displacement from axes of symmetry.
def lips(top_lip, bottom_lip, axis):
    pass
# Given the set of data from the eyebrows, compare ratio of width and 
# height to that of the other, as well as the golden ratio, and
# displacement from semi-major axis.
def brows(left_eyebrow, right_eyebrow, axis):
    pass

# finally, the golden ratio comparision of the nose
def nose(nose_tip, nose_bridge):
    pass
