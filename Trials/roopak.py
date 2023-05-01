from rtree import index
p = index.Property()
p.dimension = 1000
p.dat_extension = 'data'
p.idx_extension = 'index'  
idx32 = index.Index('3d_index',properties=p)

a = [0]*1000
b = [i for i in range(1000)]
c = [i for i in range(1000,2000)]

idx32.insert(1, tuple(a), obj=42)
idx32.insert(2, tuple(b), obj=42)
hits = list(idx32.intersection( tuple(a+c), objects=True))

# hits.nearest

for item in hits:
    print(item.id, item.object, item.bbox)