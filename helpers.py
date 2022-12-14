# Helper functions

import os
import glob # library for loading images from a directory
import matplotlib.image as mpimg



# This function loads in images and their labels and places them in a list
# The list contains all images and their associated string and numeric labels

def load_dataset(image_dir):

    # Populate this empty image list
    im_list = []
    image_types = ["red", "yellow", "green"]
    numeric_labels = [[1,0,0], [0,1,0], [0,0,1]]

    # Iterate through each color folder
    for i in range(len(image_types)):
        im_type = image_types[i]
        # Iterate through each image file in each image_type folder
        # glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):

            # Read in the image
            im = mpimg.imread(file)

            # Check if the image exists/if it's been correctly read-in
            if not im is None:
                # Append the image, and it's numeric label (red, green, yellow) to the image list
                im_list.append((im, numeric_labels[i], im_type))

    return im_list
