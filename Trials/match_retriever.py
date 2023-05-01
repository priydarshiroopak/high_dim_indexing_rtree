import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image
import pickle

from Model.rtree import index
from image_viewer import ImageViewer

# Constants
IMAGES_DIR = 'Data/Images/'

#load the data
points = np.load('Data/features.npy')
insert_count = min(100, len(points))
dim = points.shape[2]   ##
print(f'Dimension: {dim}')



img_files = pd.read_csv('Data/mapping.csv')
idx = None
# load index using pickle
with open('my_index.pickle', 'rb') as f:
    idx = pickle.load(f)
    
min_b = [-1000]*dim
max_b = [1000]*dim

print("Number of data points in the index:", idx.count(min_b+max_b))




# # Find the M nearest point to a given point
M = 4
while True:
    query_indx = int(input('Enter a index: '))
    if query_indx==-1: 
        print("Bye!")
        break
    query_point = points[query_indx][0]
    print(len(query_point))
    nearest = list(idx.nearest(tuple(query_point), M))
  
    print("Nearest: ", nearest)
    
    query_img = IMAGES_DIR+img_files.iloc[query_indx]['filename']
    print("Query image: ", query_img)
    matched_imgs = []
    
    for i in range(M):
        matched_imgs.append(IMAGES_DIR+img_files.iloc[nearest[i]]['filename'])
        print("Matched image: ", matched_imgs[i])
    
    ImageViewer(query_img, matched_imgs)
        
        
    print("\n")