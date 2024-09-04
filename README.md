# Duplicate File Finder

This Python script helps you find and manage duplicate files across multiple directories on your system. It compares files by size and then by their SHA-256 hash to identify duplicates. The user can then decide which duplicate files to keep and which to delete.

## Features

- Scans specified directories for duplicate files.
- Excludes specified folders and file types from the search.
- Uses SHA-256 hashing to accurately identify duplicate files.
- Allows the user to choose which duplicate files to keep or delete.

## How It Works

1. **Grouping by File Size**: The script first groups files by their size. Files with unique sizes are ignored.
2. **Hashing**: For files that have the same size, the script calculates the SHA-256 hash to confirm duplicates.
3. **User Interaction**: The script then prompts the user to decide which files to keep and which to delete.

## Prerequisites

- Python 3.x
- The script uses standard Python libraries (`os`, `hashlib`, `collections`).

## Installation

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/yourusername/duplicate-file-detector.git
cd duplicate-file-detector
```

## Usage

1. Open the script file `duplicate_file_detector.py`.
2. Modify the `directories`, `exclude_folders`, and `skip_extensions` lists to fit your requirements.
   - **directories**: List of directories to search for duplicates.
   - **exclude_folders**: List of folders to exclude from the search.
   - **skip_extensions**: Set of file extensions to skip during the search.
3. Run the script:

```bash
python duplicate_file_detector.py
```

4. Follow the prompts to handle the detected duplicate files.

## Example

```python
# Specify directories to search
directories = ["C:\\", "D:\\", "E:\\"]

# Specify folders to exclude
exclude_folders = ["E:\\Music"]

# Specify extensions to skip
skip_extensions = {".tmp", ".log", ".bak", ".dll", ".exe", ".sys"}
```

## Notes

- Be careful when deleting files, as this action cannot be undone.
- The script currently handles duplicate detection on a single machine and may take some time depending on the number of files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.