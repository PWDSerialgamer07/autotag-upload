import pandas as pd
import os
import numpy as np
from PIL import Image
"""
Calculate the treshold for when you wish to separate B type pictures from A type pictures automatically.
Make sure you have a set that's already separated, for calculating the threshold and testing your classifier's accuracy.
"""
TYPEA_FOLDER = "test/anime"  # Change these
TYPEB_FOLDER = "test/non-anime"


# Feel free to use your own function
def calculate_grayscale_variance(image_path) -> float:
    # Convert to grayscale and normalize to [0, 1]
    img = Image.open(image_path).convert("L")  # 'L' mode = grayscale
    img = img.resize((256, 256))  # Standardize size for consistency
    pixels = np.array(img, dtype=np.float32) / 255.0
    return np.var(pixels)


def main() -> None:
    data = []
    # Collect variance for all type A
    for img in os.listdir(TYPEA_FOLDER):
        img_path = os.path.join(TYPEA_FOLDER, img)
        variance = calculate_grayscale_variance(img_path)
        data.append({"file": img, "variance": variance,
                    "is_typeA": True})  # Label your data!
    # Collect variance for all type B
    for img in os.listdir(TYPEB_FOLDER):
        img_path = os.path.join(TYPEB_FOLDER, img)
        variance = calculate_grayscale_variance(img_path)
        data.append({"file": img, "variance": variance, "is_typeA": False})

    # Create a DataFrame and analyze
    df = pd.DataFrame(data)
    print(df.groupby("is_typeA")["variance"].describe())
