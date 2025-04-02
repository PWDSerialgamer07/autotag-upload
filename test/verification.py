import os
import shutil

"""
Get a list of all non anime images's names (with extension) and put them in test_list.txt with one per line.
"""


def main() -> None:
    os.makedirs("test", exist_ok=True)
    os.makedirs("test/false_positive", exist_ok=True)
    os.makedirs("test/undetected", exist_ok=True)
    total = 0
    for i in os.listdir("input"):
        total += 1
    for i in os.listdir("non_anime"):
        total += 1
    success = []
    false_positive = []
    undetected = []
    with open("test/test_list.txt", "r") as f:
        na = f.read()
    na = na.split("\n")
    anime = os.listdir("input")
    non_anime = os.listdir("non_anime")
    for i in non_anime:
        if i in na:
            success.append(i)
        else:
            false_positive.append(i)
            shutil.copy(os.path.join("non_anime", i), "test/false_positive")
    for i in anime:
        if i in na:
            undetected.append(i)
            shutil.copy(os.path.join("input", i), "test/undetected")
        else:
            success.append(i)
    print(f"Success: {len(success)}/{total}")
    print(f"False Positive: {len(false_positive)}/{total}")
    print(f"Undetected: {len(undetected)}/{total}")


if "__main__" == __name__:
    main()
