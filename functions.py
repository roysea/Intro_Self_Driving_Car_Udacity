# Main functions for the project are within this file
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 # opencv-python (computer vision) library to visualize images
import numpy as np

def show_single_rgb_image(img):
    if img is not None:
        im = img[0]
        label = "Label: " + img[2]

        plt.imshow(im)
        plt.title(label)
    else:
        print("Image file is empty!")


def unify_image_size(img, size):
    # create a copy of image, Resize image to 32 x 32 and return the new image
    return cv2.resize(np.copy(img), (size, size))


def standardize(image_list, size):
    if len(image_list):
        # standard list will include tuple: (image matrix, numberic label)
        standard_list = []
        for img in image_list:
            standard_list.append((unify_image_size(img[0], size), img[1]))
        return standard_list

    else:
        return print("Image list is empty!")


def visualize_std_vs_original_images(image_list, std_list, img_indices):
    # make sure there are some indices to check
    if img_indices is not None:
        # make sure lists are not empty and sizes match
        if len(image_list) and len(std_list) and len(image_list) == len(std_list):
            num_images = len(img_indices)
            f, ax = plt.subplots(num_images, 2, figsize=(10, 15))
            for i in range(len(img_indices)):
                ax[i, 0].set_title("Original Image: " + image_list[img_indices[i]][2])
                ax[i, 0].imshow(image_list[img_indices[i]][0])

                label = "Standard Image: "
                if std_list[img_indices[i]][1] == [1,0,0]:
                    label += "Red [1,0,0]"
                elif std_list[img_indices[i]][1] == [0,1,0]:
                    label += "Yellow [0,1,0]"
                else:
                    label += "Green [0,0,1]"

                ax[i, 1].set_title(label)
                ax[i, 1].imshow(std_list[img_indices[i]][0])
        else:
            print("we cannot compare both lists, because their length are different!")
    else:
        print("Please add some image indices to the img_indices list!")
