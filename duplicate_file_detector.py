import os
import hashlib
from collections import defaultdict

def get_file_hash(file_path, block_size=65536):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except (OSError, IOError) as e:
        print(f"Could not open/read file: {file_path}. Error: {e}")
        return None

def find_duplicate_files(directories, exclude_folders, skip_extensions):
    """Find and list duplicate files, skipping specified extensions."""
    files_by_size = defaultdict(list)
    duplicates = defaultdict(list)
    
    # First pass: Group files by size
    for directory in directories:
        for root, _, files in os.walk(directory):
            if any(excluded in root for excluded in exclude_folders):
                continue

            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in skip_extensions:
                    continue  # Skip files with specified extensions
                
                try:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    files_by_size[file_size].append(file_path)
                except (OSError, IOError):
                    continue

    # Second pass: Hash files with the same size
    for file_list in files_by_size.values():
        if len(file_list) < 2:
            continue  # Skip if there's only one file of this size

        for file_path in file_list:
            file_hash = get_file_hash(file_path)
            if file_hash:
                duplicates[file_hash].append(file_path)

    return [files for files in duplicates.values() if len(files) > 1]

def handle_duplicates(duplicates):
    """Allow the user to handle duplicates in a batch process."""
    for duplicate_group in duplicates:
        print("\nDuplicate group found:")
        for i, file_path in enumerate(duplicate_group, 1):
            print(f"{i}: {file_path}")

        choice = input("Enter the number of the file you want to keep (or 'all' to keep all): ")

        if choice.isdigit():
            keep_index = int(choice) - 1
            for i, file_path in enumerate(duplicate_group):
                if i != keep_index:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
        elif choice.lower() != 'all':
            print("Invalid choice, skipping this group...")

if __name__ == "__main__":
    # Specify directories to search
    directories = ["C:\\", "D:\\"]  # Add or modify drive letters

    # Specify folders to exclude
    exclude_folders = [  "E:\\Music", "E:\\server stuffs"]  # Modify as needed

    # Specify extensions to skip
    skip_extensions = {".tmp", ".log", ".bak", ".dll", ".exe", ".sys"}  # Add or modify extensions to skip

    duplicates = find_duplicate_files(directories, exclude_folders, skip_extensions)
    
    if duplicates:
        handle_duplicates(duplicates)
    else:
        print("No duplicates found.")
