import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image, ImageTk
from random import random
import tkinter as tk
from tkinter import filedialog
import os

from Model.rtree import index
from image_viewer import ImageViewer


from Model.featureExtractor import FeatureExtractor


# Constants
IMAGES_DIR = 'Data/Images/'

#load the data
points = np.load('Data/features.npy')
img_files = pd.read_csv('Data/mapping.csv')
insert_count = 100
dim = points.shape[2]   ##
print(f'Dimension: {dim}')

p = index.Property()
p.dimension = dim


# Create the rtree index for dim-dimensional data
idx = index.Index(properties=p)


# Insert some points into the index
for i in tqdm(range(insert_count)):
    idx.insert(i, tuple(points[i][0]))
    
match_count = 4
def get_matched_images(query_vector):
    nearest = list(idx.nearest(tuple(query_vector), match_count))
    matched_imgs = []
    for i in range(match_count):
        matched_imgs.append(IMAGES_DIR+img_files.iloc[nearest[i]]['filename'])
    return matched_imgs
    
# initialise the feature extractor
obj = FeatureExtractor()


    
# # Find the M nearest point to a given point
M = 4
while True:
    file_path = input('Enter an image File path: ')
    if file_path=='exit': 
        print("Bye!")
        break
    
    img = Image.open(file_path)
    img_features = obj.extract_features(np.array(img))
    
    
    print("Query image: ", file_path)
    matched_imgs = get_matched_images(img_features)
    
    print("Matched images: ", matched_imgs)
    

    ImageViewer(file_path, matched_imgs)
        
        
    print("\n")