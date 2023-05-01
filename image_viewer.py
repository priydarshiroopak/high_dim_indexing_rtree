import matplotlib.pyplot as plt

def ImageViewer(query_img, matched_imgs):
    # Load query image and matching images
    n = len(matched_imgs)
    query_image = plt.imread(query_img)
    matching_images = [plt.imread(matched_imgs[i]) for i in range(n)]

    # Create a figure with 2 rows and 4 columns
    fig, axes = plt.subplots(nrows=2, ncols=n, figsize=(10,6))

    # Display the query image in the first subplot of the first row
    axes[0, 0].imshow(query_image)
    axes[0, 0].set_title('Query Image')

    # Display the matching images in the subplots of the second row
    for i, matching_image in enumerate(matching_images):
        axes[1, i].imshow(matching_image)
        axes[1, i].set_title(f'Matching Image {i+1}')

    # Turn off axis labels
    for ax in axes.flatten():
        ax.axis('off')

    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.3, wspace=0.1)

    # Show the figure
    plt.show()
    

# query_img = 'img1.jpeg'
# matched_imgs = ['img1.jpeg']*4
# ImageViewer(query_img, matched_imgs)
