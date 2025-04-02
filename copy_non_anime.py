import shutil
import os

with os.open("test/test_list.txt", "r") as f:
    na = f.read()
non_anime = na.split("\n")
anime = os.listdir("input")
for i in anime:
    shutil.copy(os.path.join("input", i), "test/anime")
for j in non_anime:
    shutil.copy(os.path.join("test/anime", i), "test/non-anime")
