# Authors: Bogdan Marinski, Konstantin Boev
# Version: 1.0.0 (30.04.2020)

def get_color(path_to_image):

    # This function accepts a path to an image and returns it's color and a path to generated color masks

    import cv2
    import numpy as np
    import os

    current_image = cv2.imread(path_to_image, 1)  #loads an image as a color image
    hsv = cv2.cvtColor(current_image, cv2.COLOR_BGR2HSV)  #converts the image to HSV (hue-saturation-value) color space

    # changes the current directory to the temp for writing masks
    temp_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'temp'))
    os.chdir(temp_dir) 

    # color thresholds [H, S, V]
    lower_yellow = np.array([ 20, 70, 120])
    upper_yellow = np.array([ 30, 255, 255])
    
    lower_green = np.array([ 35, 25, 25])
    upper_green = np.array([ 70, 255, 255])

    lower_red = np.array([ 0, 50, 120])
    upper_red = np.array([ 10, 255, 255])

    lower_red2 = np.array([ 170, 145, 210])
    upper_red2 = np.array([ 180, 230, 220])

    lower_blue = np.array([ 90, 60, 0])
    upper_blue = np.array([ 121, 255, 255])

    lower_white = np.array([0,0,128])
    upper_white = np.array([0,0,225])

    # generating masks for each color from the image and the thresholds
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    # writes the color masks to the temp folder
    cv2.imwrite("mask_yellow.png", mask_yellow)
    cv2.imwrite("mask_green.png", mask_green)
    cv2.imwrite("mask_red.png", mask_red)
    cv2.imwrite("mask_red2.png", mask_red2)
    cv2.imwrite("mask_blue.png", mask_blue)
    cv2.imwrite("mask_white.png", mask_white)

    # count the non-zero pixel count for each mask
    yellow_pixel_count = cv2.countNonZero(mask_yellow)
    green_pixel_count = cv2.countNonZero(mask_green)
    red_pixel_count = cv2.countNonZero(mask_red)
    red2_pixel_count = cv2.countNonZero(mask_red2)
    blue_pixel_count = cv2.countNonZero(mask_blue)
    white_pixel_count = cv2.countNonZero(mask_white)

    pixel_count_list = np.array([yellow_pixel_count, green_pixel_count, red_pixel_count, red2_pixel_count, blue_pixel_count, white_pixel_count])
    dominant_pixel_count = np.argmax(pixel_count_list)  #returns the index of the element with the biggest value

    color_dictionary = {-1:'error/defect', 0:'yellow', 1:'green', 2:'red', 3:'red', 4:'blue', 5:'white'}

    # check for minimal colored pixels count threshold
    if pixel_count_list[dominant_pixel_count] > 1000:
        return([str(color_dictionary[dominant_pixel_count]), str(temp_dir), str(yellow_pixel_count), str(green_pixel_count), str(red_pixel_count), str(red2_pixel_count), str(blue_pixel_count), str(white_pixel_count)])
    else:
        return([str(color_dictionary[-1]), str(temp_dir), str(yellow_pixel_count), str(green_pixel_count), str(red_pixel_count), str(red2_pixel_count), str(blue_pixel_count), str(white_pixel_count)])
