import re

def tokenize_message(message: str):
    """Tokenize message into meaningful chunks."""
    return re.findall(r"[\w@]+", message)

def compression_ratio(original: str, encoded: str):
    """Calculate compression ratio achieved."""
    if not original:
        return 0
    return round(100 * (1 - len(encoded)/len(original)), 2)

