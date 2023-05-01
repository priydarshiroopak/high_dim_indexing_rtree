import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image

from Model.rtree import index
from image_viewer import ImageViewer

# Constants
IMAGES_DIR = 'Data/Images/'

#load the data
points = np.load('Data/features.npy')
insert_count = min(100, len(points))
dim = points.shape[2]   ##
print(f'Dimension: {dim}')

# index properties
p = index.Property()
p.dimension = dim
# p.dat_extension = 'data'
# p.idx_extension = 'index'

img_files = pd.read_csv('Data/mapping.csv')

# Create the rtree index for dim-dimensional data
idx = index.Index(properties=p)

# Insert some points into the index
for i in tqdm(range(insert_count)):
    idx.insert(i, tuple(points[i][0]), obj=42)
    

# save idx using pickle
import pickle


# write the object to a file
with open('my_index.pickle', 'wb') as f:
    pickle.dump(idx, f)     

min_b = [-1000]*dim
max_b = [1000]*dim

print("Number of data points in the index:", idx.count(min_b+max_b))
    
    
