"""
For each image:
1. If Option 2 (histogram) → "likely non-anime" → skip.
2. Else → run DeepDanbooru.
3. If DeepDanbooru confidence is low → flag as non-anime.
"""

import matplotlib.pyplot as plt  # importing matplotlib
import os
import cv2
import numpy as np
import shutil
from PIL import Image

INPUT_FOLDER: str = "input"
NON_ANIME_FOLDER: str = "non_anime"
UNSURE_FOLDER: str = "unsure"
THRESHOLD: float = 0.03


def histogram_debug(img_path) -> bool:
    img = Image.open(img_path)
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original")

    # Plot grayscale histogram
    plt.subplot(1, 2, 2)
    gray_img = img.convert("L")
    plt.hist(np.array(gray_img).flatten(), bins=50, color="black")
    plt.title("Grayscale Histogram")
    plt.show()


def calculate_grayscale_variance(img_path):
    # Convert to grayscale and normalize to [0, 1]
    img = Image.open(img_path).convert("L")  # 'L' mode = grayscale
    img = img.resize((256, 256))  # Standardize size for consistency
    pixels = np.array(img, dtype=np.float32) / 255.0
    return np.var(pixels)


def histogram(img_path) -> bool:
    variance = calculate_grayscale_variance(img_path)
    return variance < THRESHOLD


def danbooru_check(img_path) -> bool:
    pass


def main() -> None:
    os.makedirs(NON_ANIME_FOLDER, exist_ok=True)
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(UNSURE_FOLDER, exist_ok=True)
    if os.listdir(INPUT_FOLDER) == []:
        print("No images in input folder.")
        input("Press enter to exit.")
        exit()

    for img in os.listdir(INPUT_FOLDER):
        img_path = os.path.join(INPUT_FOLDER, img)
        if histogram(img_path):
            shutil.move(img_path, NON_ANIME_FOLDER)
        else:
            danbooru_check(img_path)


if __name__ == "__main__":
    main()
