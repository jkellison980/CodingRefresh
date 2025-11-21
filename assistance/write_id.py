import json
import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = BASE_DIR / "data" / "trait_list.json"



def sha256_id(name:str) -> str:
    return hashlib.sha256(name.encode("utf-8")).hexdigest()

def update_trait_id(json_path: Path):
    if not json_path.exists():
        raise FileNotFoundError("JSON FILE NOT FOUND")
    
    # Load the file
    with json_path.open("r") as f:
        data = json.load(f)

    traits = data.get("traits", [])

    for trait in traits:
        name = trait.get("name")
        if not name:
            print("Skipping entry with no name: ", trait)
            continue
        
        new_hash = sha256_id(name)

        # Skip if it exists
        if trait.get("id") == new_hash:
            continue

        # Write is does not exist/needs updating
        trait["id"] = new_hash
        print(f"Updated ID for '{name}' → {new_hash}")

    with json_path.open("w") as f:
        json.dump(data, f, indent=1)
        f.write("\n")
    
    print("\nJSON updated successfully")

if __name__ == "__main__":
    update_trait_id(JSON_PATH)