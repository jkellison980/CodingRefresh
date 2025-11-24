from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class Item:
    id: str
    name: str
    type: str
    rarity: str
    description: str
    value: int

    stats: Dict[str, Any] = field(default_factory=dict)
    effects: Dict[str, Any] = field(default_factory=dict)