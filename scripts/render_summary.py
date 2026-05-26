import json
from pathlib import Path

RESULTS_DIR = Path("results")

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def summarize(file):
    data = load_jsonl(file)

    summary = {
        "file": str(file),
        "total_records": len(data),
        "status_counts": {}
    }

    for item in data:
        status = item.get("status", "unknown")
        summary["status_counts"][status] = summary["status_counts"].get(status, 0) + 1

    return summary

def main():
    print("=== SUMMARY GENERATION START ===")

    summaries = []

    for file in RESULTS_DIR.glob("*.jsonl"):
        print(f"Processing {file}")
        summaries.append(summarize(file))

    output_path = Path("metadata") / "execution_summary.json"

    Path("metadata").mkdir(exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(summaries, f, indent=2)

    print(f"\nSummary written to: {output_path}")
    print("=== SUMMARY COMPLETE ===")

if __name__ == "__main__":
    main()
