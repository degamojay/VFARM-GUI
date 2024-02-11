import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import numpy as np

class VolumetricRepresentation:
    def __init__(self, image_path):
        self.fig = self.create_volumetric_visualization(image_path)

    def create_volumetric_visualization(self, image_path):
        original_image = Image.open(image_path).convert('L')
        processed_image = original_image.filter(ImageFilter.FIND_EDGES)
        image_array = 255 - np.array(processed_image)
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.imshow(image_array, cmap='viridis', origin='upper')
        return fig
