import shutil
import os

for i in os.listdir("non_anime"):
    shutil.move(os.path.join("non_anime", i), "input")
