# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import zipfile


# Part 1


def clean_cache():
    path = "files/cache"
    if not os.path.exists(path):
        os.mkdir(path)
        print("Folder created bro.")
    else:
        for file_name in os.listdir(path):
            os.remove(os.path.join(path, file_name))


# Part 2


def cache_zip(zip_file_path, cache_dir_path):
    from zipfile import ZipFile

    with ZipFile(zip_file_path, "r") as f:
        f.extractall(cache_dir_path)


# Part 3


def cached_files():
    path = r"C:\Users\evisi\Desktop\Winc\files\cache"
    files_in_cache = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files_in_cache.append(os.path.join(path, item))
    return files_in_cache


# Part 4


def find_password(cached_files):
    password = "password"
    for file in cached_files:
        with open(file, "r") as f:
            for line in f:
                if password in line:
                    line = line.replace("password:", "").strip()
                    return line
