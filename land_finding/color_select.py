# Run python color_select.py and a test-after.jpg will be saved for filtering out other colors only leave the lanes
# https://classroom.udacity.com/courses/ud013-preview/lessons/ca4dcf64-537a-49c7-9fbb-946c968174a9/concepts/b180303f-be20-4b38-a3d3-aa0ffe8d3ea0
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
image = mpimg.imread('test.jpg')

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)

# Define color selection criteria
###### MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
# I would write a loop and try different combos and save all the images and keep the best results
red_threshold = 200
green_threshold = 200
blue_threshold = 200
######

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

print image # 3 dimensional array
# Do a boolean or with the "|" character to identify
# pixels below the thresholds
thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
print thresholds
color_select[thresholds] = [0,0,0]

# Display the image
plt.imshow(color_select)

# Uncomment the following code if you are running the code locally and wish to save the image
mpimg.imsave("test-after.png", color_select)
