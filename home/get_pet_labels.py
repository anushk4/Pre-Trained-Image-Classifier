#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

# Imports python modules
from os import listdir

def getfilelabel(name):
    namelist = name.lower().split("_")
    pet = ""
    for i in namelist:
        if i.isalpha():
            pet += i + " "
    return [pet.strip()]
 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    files = listdir(image_dir)
    result_dic = dict()
    for filename in files:
        if filename[0] == ".":
            continue
        if filename not in result_dic:
            result_dic[filename] = getfilelabel(filename)
        else:
            print("Warning: {} already exists with label {}".format(filename,result_dic[filename]))
    return result_dic
