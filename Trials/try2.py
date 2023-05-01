import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Set the names of the image files
query_image_file = 'img1.jpeg'
matched_image_files = ['img1.jpeg']*4

# Load the images using imread()
query_image = mpimg.imread(query_image_file)
matched_images = [mpimg.imread(filename) for filename in matched_image_files]

# Create the first plot with the query image in the center of the first row
fig1 = plt.figure(figsize=(6, 3))
ax1 = fig1.add_subplot(1, 3, 2)
ax1.imshow(query_image)
ax1.set_title('Query Image')
ax1.set_xticks([])
ax1.set_yticks([])
plt.subplots_adjust(wspace=0.05)

# Create the second plot with the matched images in the second row
fig2 = plt.figure(figsize=(6, 3))
for i in range(4):
    ax2 = fig2.add_subplot(1, 4, i+1)
    ax2.imshow(matched_images[i])
    ax2.set_title(f'Matched Image {i+1}')
    ax2.set_xticks([])
    ax2.set_yticks([])
plt.subplots_adjust(wspace=0.05)

# Show the plots
plt.show()
