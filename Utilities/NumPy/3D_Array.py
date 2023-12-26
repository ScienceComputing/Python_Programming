import numpy as np
rgb_1 = np.array([
                  [[255, 0, 0], [255, 255, 0], [255, 255, 255]],
               		[[255, 0, 255], [0, 255, 0], [0, 255, 255]],
               		[[0, 0, 0], [0, 255, 255], [0, 0, 255]]
                 ])

# Change the first element (red value) of the above array to 128
rgb_1[0, 0, 0] = 128

# Change the last element (blue value) of the above array to 0
rgb_1[-1, -1, 2] = 0

# Update all green values above 150 to 150
rgb_1[rgb_1[:, :, 1] > 150, 1] = 150 # The second 1 refers to the green channel of the RGB array.

rgb_1
# array([[[128,   0,   0],
#         [255, 150,   0],
#         [255, 150, 255]],

#        [[255,   0, 255],
#         [  0, 150,   0],
#         [  0, 150, 255]],

#        [[  0,   0,   0],
#         [  0, 150, 255],
#         [  0,   0,   0]]])

# Update all 0 values with 255
rgb_1 = np.where(rgb_1 == 0, 255, rgb_1)

# Update all colors represented by 1-d array [0, 150, 255] with [97, 12, 228]
rgb_1 = np.where(rgb_1 == [0, 150, 255], [97, 12, 228], rgb_1)

# Visualize the image
import matplotlib.pyplot as plt
plt.imshow(rgb_1)
plt.show()
