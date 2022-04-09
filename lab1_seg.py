import numpy as np
from cv2 import cv2
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets._samples_generator import make_blobs
from itertools import cycle
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

image = cv2.imread("kmean.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img = np.array(image)
# saving the image shape
shape = img.shape
print(shape)
# reshaping image
reshape_img = np.reshape(img, [-1, 3])
print(reshape_img)
# plotting the image
print(plt.imshow(img))
plt.title(img.shape)
bandwidth = estimate_bandwidth(reshape_img, quantile=0.1, n_samples=100)
msc = MeanShift(bandwidth=bandwidth, bin_seeding=True)
msc.fit(reshape_img)
print("shape of labels : %d" % msc.labels_.shape)
print( msc.cluster_centers_.shape)
print("number of estimated clusters : %d" % len(np.unique(msc.labels_)))
labels = msc.labels_
result_image = np.reshape(labels, shape[:2])
fig = plt.figure(2, figsize=(14, 12))
ax = fig.add_subplot(121)
ax = plt.imshow(img)
ax = fig.add_subplot(122)
ax = plt.imshow(result_image)
plt.show()