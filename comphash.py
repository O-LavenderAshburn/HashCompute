import os
import hashlib

def compute_hashes(file_path):
    """Compute MD5 and SHA256 for a given file."""
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  # Read in chunks to handle large files
                md5_hash.update(chunk)
                sha256_hash.update(chunk)
        return md5_hash.hexdigest(), sha256_hash.hexdigest()
    except Exception as e:
        return None, None  # Could not read file

def hash_files_in_directory(directory):
    """Walk through the directory and print hashes for each file."""
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            md5, sha256 = compute_hashes(full_path)
            if md5 and sha256:
                print(f"Name: {full_path} MD5: {md5} SHA256: {sha256}")
            else:
                print(f"Name: {full_path} ERROR: Could not read file.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python hash_files.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        hash_files_in_directory(directory_path)
