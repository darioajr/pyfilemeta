import os
import hashlib
import mimetypes
from datetime import datetime

def get_file_metadata(file_path):
    """Returns the metadata of a file."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return {
        "file_name": os.path.basename(file_path),
        "size_bytes": os.path.getsize(file_path),
        "created_at": datetime.fromtimestamp(os.path.getctime(file_path)).isoformat(),
        "modified_at": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat(),
        "mime_type": mimetypes.guess_type(file_path)[0] or "Unknown",
        "hashes": {
            "md5": get_file_hash(file_path, "md5"),
            "sha256": get_file_hash(file_path, "sha256"),
        },
    }

def get_file_hash(file_path, algorithm="md5"):
    """Calculates the hash of the file using the specified algorithm (md5, sha256)."""
    hash_func = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()
