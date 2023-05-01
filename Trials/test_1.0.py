from Model.rtree import index
from Data.generateRandom import points, dimension as dim

# Create the rtree index for 6-dimensional data
idx = index.Index(properties=index.Property(dimension=dim))

# Insert some points into the index
for i in range(len(points)):
    idx.insert(i, tuple(points[i]))
    

# Find the nearest point to a given point
query_point = [3.4]*dim
nearest = list(idx.nearest(tuple(query_point), 1))
print(nearest)

query_point = [-3]*dim
nearest = list(idx.nearest(tuple(query_point), 1))
print(nearest)


query_point = [i for i in range(dim)]
nearest = list(idx.nearest(tuple(query_point), 1))
print(nearest)