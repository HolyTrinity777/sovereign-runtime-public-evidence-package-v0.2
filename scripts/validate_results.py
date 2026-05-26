import json
from pathlib import Path

RESULTS_DIR = Path("results")
DATASETS_DIR = Path("datasets")

def load_jsonl(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data

def validate_structure(obj):
    required_keys = ["test_id", "status"]  # minimal schema expectation
    return all(k in obj for k in required_keys)

def main():
    print("=== RESULT VALIDATION START ===")

    if not RESULTS_DIR.exists():
        print("No results directory found.")
        return

    for file in RESULTS_DIR.glob("*.jsonl"):
        print(f"\nValidating {file}")
        data = load_jsonl(file)

        total = len(data)
        valid = sum(validate_structure(x) for x in data)

        print(f"Total entries: {total}")
        print(f"Valid entries: {valid}")
        print(f"Schema pass rate: {valid/total if total else 0:.2f}")

    print("\n=== VALIDATION COMPLETE ===")

if __name__ == "__main__":
    main()
