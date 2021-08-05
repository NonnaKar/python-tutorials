import pathlib
from os import scandir
from datetime import datetime
from pathlib import Path

# Example 1
with open('data.txt', 'r') as f:
    data = f.read()

# Example 2
with open("data.txt", 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)

# Example 3
import os

entries = os.listdir('my_directory/')
for entry in entries:
    print(entry)

# Example 4

entries = os.scandir('my_directory/')
print(entries)

# Example 5

entries = Path('my_directory/')
for entry in entries.iterdir():
    print(entry.name)

# Example 6
# * List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

# Example 7
# * List all files in a directory using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# Example 8

basepath = Path('my_directory/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)

# Example 9

with os.scandir('my_directory/') as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)

# Example 10

current_dir = Path('my_directory')
for path in current_dir.iterdir():
    info = path.stat()
    print(info.st_mtime)

# Example 11


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def get_files():
    dir_entries = scandir('my_directory/')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')


# Example 12
os.mkdir('example_directory/')

# Example 13

p = Path('example_directory/')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)

# Example 14
os.makedirs('2019/10/05', mode=0o770)

# Example 15

p = pathlib.Path('2018/10/05')
p.mkdir(parents=True)
