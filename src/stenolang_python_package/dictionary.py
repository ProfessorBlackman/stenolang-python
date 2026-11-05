import json
from pathlib import Path

BASE_DICTIONARY = {
    "@ok": "success",
    "@er": "error",
    "@rq": "request",
    "@rs": "response",
    "@dt": "data",
    "@id": "identifier",
    "@up": "update",
    "@rm": "remove"
}

def load_dictionary(custom_dict_path=None):
    """Merge base dictionary with custom domain dictionary."""
    merged = BASE_DICTIONARY.copy()
    if custom_dict_path:
        path = Path(custom_dict_path)
        if path.exists():
            with open(path, "r") as f:
                user_dict = json.load(f)
                merged.update(user_dict)
    return merged
