import pandas as pd
import os
from PIL import Image
import numpy as np
import cv2
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
#s


labels_df = pd.read_csv('labels_cleaned.csv') 
labels_df['inverted'] = False
print(labels_df.head())

image_dir = '../Images\\train\\' 
def load_image(image_name):
    file_extension = '.jpeg'
    filename = f"{image_name}{file_extension}"
    file_path = os.path.join(image_dir, filename)
    return Image.open(file_path)

for i in range (1):
    sample_image = load_image(labels_df.iloc[i]['image'])
    sample_image.show()
