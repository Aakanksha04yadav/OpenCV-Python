
import matplotlib.pyplot as plt
 
plt.imshow(img)
plt.title('Displaying image using Matplotlib')
plt.show()

# Displays the entire Image


#Using OpenCV:
from cv2 import imshow, waitKey
 
imshow('Displaying image using OpenCV', img) 
waitKey(0)
