import json
import hashlib
from pathlib import Path

HASHABLE_LIST_KEYS = ["traits","items"]

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = [
    BASE_DIR / "data" / "trait_list.json",
    BASE_DIR / "data" / "items.json"
]


def sha256_id(name:str) -> str:
    return hashlib.sha256(name.encode("utf-8")).hexdigest()

def update_trait_id(json_path: Path):
    if not json_path.exists():
        raise FileNotFoundError(f"[ERROR] File not found: {json_path}")
    
    # Load the file
    with open(json_path, "r") as f:
        data = json.load(f)

    target_key = None
    for key in HASHABLE_LIST_KEYS:
        if key in data:          # <-- FIX: your version always used the first key blindly
            target_key = key
            break

    if not target_key:
        print(f"[SKIPPED] No supported list key found in {json_path.name}")
        return

    for obj in data[target_key]:
        if "name" not in obj:
            print(f"[WARNING] Entry missing 'name' in {json_path.name}: {obj}")
            continue

        obj["id"] = sha256_id(obj["name"])

    with open(json_path,"w") as f:
        json.dump(data, f, indent=1)
        f.write("\n")
    
    print(f"[OK] Updated entries in {json_path.name} ({target_key})")

def process_all_files():
    print("### Updating ID hashes ###")
    for file_path in JSON_PATH:
        update_trait_id(file_path)
    print("=== Done ===")

if __name__ == "__main__":
    process_all_files()