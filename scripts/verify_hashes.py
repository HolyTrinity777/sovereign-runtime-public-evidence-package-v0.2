import hashlib
import json
import os
from pathlib import Path

DATASET_DIR = Path("datasets")
RESULTS_DIR = Path("results")
METADATA_DIR = Path("metadata")

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def load_manifest():
    manifest_path = DATASET_DIR / "DATASET_MANIFEST.json"
    if not manifest_path.exists():
        print("No dataset manifest found.")
        return None
    with open(manifest_path) as f:
        return json.load(f)

def verify_directory(path):
    print(f"\nVerifying: {path}")
    for file in path.rglob("*"):
        if file.is_file():
            print(f"{file}: {sha256_file(file)}")

def main():
    print("=== HASH VERIFICATION START ===")

    if DATASET_DIR.exists():
        verify_directory(DATASET_DIR)

    if RESULTS_DIR.exists():
        verify_directory(RESULTS_DIR)

    if METADATA_DIR.exists():
        verify_directory(METADATA_DIR)

    manifest = load_manifest()
    if manifest:
        print("\nManifest loaded successfully.")

    print("=== HASH VERIFICATION COMPLETE ===")

if __name__ == "__main__":
    main()
