# file_renamer.py

import os
import argparse
import datetime

def rename_files(directory, prefix='', suffix='', add_date=False):
    files = os.listdir(directory)
    for count, filename in enumerate(files):
        file_path = os.path.join(directory, filename)

        if not os.path.isfile(file_path):
            continue

        name, ext = os.path.splitext(filename)
        date_str = datetime.datetime.now().strftime('%Y%m%d') if add_date else ''
        new_name = f"{prefix}{date_str}_{count+1}{suffix}{ext}"
        new_path = os.path.join(directory, new_name)

        os.rename(file_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch rename files in a directory.')
    parser.add_argument('directory', help='Path to the target directory')
    parser.add_argument('--prefix', default='', help='Prefix to add to filenames')
    parser.add_argument('--suffix', default='', help='Suffix to add to filenames')
    parser.add_argument('--date', action='store_true', help='Add current date to filenames')

    args = parser.parse_args()

    rename_files(args.directory, args.prefix, args.suffix, args.date)
