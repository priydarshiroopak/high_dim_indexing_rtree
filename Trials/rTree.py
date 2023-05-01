from rtree import index
import numpy as np

# Create the rtree index for 6-dimensional data
idx = index.Index(properties=index.Property(dimension=6))

# Insert some points into the index
idx.insert(0, (0, 0, 0, 0, 0, 0))
idx.insert(1, (1, 1, 1, 1, 1, 1))
idx.insert(2, (2, 2, 2, 2, 2, 2))

# Find the nearest point to a given point
point = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
nearest = list(idx.nearest(point, 1))

# Print the results
print(nearest)
