import argparse
import os

# Path to the directory from args
parser = argparse.ArgumentParser(description='Rename files in a directory')
parser.add_argument('path', type=str, help='Path to the directory')
args = parser.parse_args()
path = args.path

# List of files in the directory
files = os.listdir(path)
for index, file in enumerate(files):
    print(index, file)
    if file.startswith('._'): #workaround for macos files
        continue
    new_name = file.replace('LRV', 'MP4')
    os.rename(os.path.join(path, file), os.path.join(path, new_name))
