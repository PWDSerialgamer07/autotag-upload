import pandas as pd
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
"""
Calculate the treshold for when you wish to separate B type pictures from A type pictures automatically.
Make sure you have a set that's already separated, for calculating the threshold and testing your classifier's accuracy.
I'm gonna go follow a data science course before continuing this so I'm not winging it as much.
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


def plot_distributions(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x="variance", hue="is_anime", kde=True, bins=50)
    plt.title("Variance Distribution: Anime vs. Non-Anime")
    plt.xlabel("Grayscale Variance")
    plt.show()


def main() -> None:
    data = []
    # Collect variance for all type A
    for img in os.listdir(TYPEA_FOLDER):
        img_path = os.path.join(TYPEA_FOLDER, img)
        variance = calculate_grayscale_variance(img_path)
        data.append({"file": img, "variance": variance,
                    "is_anime": True})  # Label your data!
    # Collect variance for all type B
    for img in os.listdir(TYPEB_FOLDER):
        img_path = os.path.join(TYPEB_FOLDER, img)
        variance = calculate_grayscale_variance(img_path)
        data.append({"file": img, "variance": variance, "is_anime": False})

    # Create a DataFrame and analyze
    df = pd.DataFrame(data)
    print(df.groupby("is_anime")["variance"].describe())


if __name__ == "__main__":
    main()
