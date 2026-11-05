def decode(encoded_message: str, dictionary: dict) -> str:
    """Decode stenographic message using the provided dictionary."""
    decoded = encoded_message
    for code, phrase in dictionary.items():
        decoded = decoded.replace(code, phrase)
    return decoded
