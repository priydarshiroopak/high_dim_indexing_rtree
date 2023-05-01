# Efficient High Dimensional Indexing/ Data Search using R-tree

## Introduction
This repository contains the code for the project on efficient high dimensional data search using R-tree. The aim of the project is to create an efficient method for storing and retrieving data points that exist in a high-dimensional space, like images and audio files that can be represented as high dimensional vectors.

## Dataset
The project focuses on image data and uses a dataset of animal images, including cats, dogs, tigers, and elephants. The dataset consists of 7000 images, but only 2000 are randomly selected and inserted into the R-tree index due to its in-memory limitations.

## Objectives
* Implement the R-tree algorithm using the official library implementation.
* Develop an efficient indexing system that can store and retrieve data points efficiently.
* Use the R-tree index to perform efficient searches on the dataset.
* Evaluate the performance of the R-Tree indexing system on the animal image dataset and compare it with other indexing systems.

## Methodology
The project involves the following steps:

### Feature Extraction: 
A deep learning model, ResNet-18, is used for extracting useful features from an image and representing it as a high dimensional vector. This process involves resizing the input image, preprocessing it to match the format expected by the ResNet-18 model, passing it through the ResNet-18 model to obtain the feature map output, flattening the feature map output into a 1D vector of features, and applying dimensionality reduction techniques such as principal component analysis (PCA) or t-distributed stochastic neighbor embedding (t-SNE) to reduce the dimensionality of the feature vector.

### R-Tree Implementation: 
The R-Tree algorithm is implemented using the official library implementation, including methods for insertion, deletion, and searching data points. The R-tree optimizes the process of searching high-dimensional data by partitioning the data space into a hierarchy of rectangular regions called "bounding boxes" or "minimum bounding rectangles" (MBRs).

## How to Use
Clone the repository using the following command:
```bash
 git clone https://github.com/priydarshiroopak/high_dim_indexing_rtree.git
```
and run the python file named 'final.py'

Note: In case `linspatialindex_c` not found error is returned during running final.py, an additional `sudo apt-get install libspatialindex-c6` may be done by the user.

# Scope of Improvement
The current implementation focuses on image data, but the methodology can be extended to other forms of multimedia data, such as audio, video, or text. Additionally, the in-memory indexing system can be improved by implementing a persistent indexing system that allows for larger datasets and multimodal data.
