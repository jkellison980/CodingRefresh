import json
from pathlib import Path

from .items import Item

REQUIRED_FIELDS = ["name", "type", "rarity", "description", "value"]

class ItemLoader:

    def __init__(self, json_path: str):
        self.json_path = Path(json_path)
        self.items = {}

    def load(self):
        if not self.json_path.exists():
            raise FileNotFoundError(f"Item file not found: {self.json_path}")

        with open(self.json_path, "r") as itemlist:
            data = json.load(itemlist)

        for item_key, item_data in data.items():
            self._validate_item(item_key, item_data)
            item = Item(**item_data)
            self.items[item.id] = item

        return self.items

    def _validate_item(self, key: str, item_data: dict):
        for field in REQUIRED_FIELDS:
            if field not in item_data:
                raise ValueError(
                    f"Item '{key}' missing required field: '{field}'"
                )