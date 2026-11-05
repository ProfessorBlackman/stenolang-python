def encode(message: str, dictionary: dict) -> str:
    """Encode message using stenographic dictionary."""
    encoded = message
    # Sort phrases by length (longest first) to avoid partial replacements
    for code, phrase in sorted(dictionary.items(), key=lambda x: len(x[1]), reverse=True):
        encoded = encoded.replace(phrase, code)
    return encoded
