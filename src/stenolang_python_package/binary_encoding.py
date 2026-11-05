def encode_binary(tokens, byte_map):
    """Convert list of tokens to bytes."""
    return bytes([byte_map[token] for token in tokens])

def decode_binary(byte_data, reverse_map):
    """Convert bytes back to tokens."""
    return [reverse_map[b] for b in byte_data]

byte_map = {
    "@rq": 0x01,
    "@pt": 0x03,
    "@dt": 0x04,
    "@up": 0x07
}
reverse_map = {v: k for k, v in byte_map.items()}

tokens = ["@rq", "@pt", "@dt", "@up"]
binary_data = encode_binary(tokens, byte_map)
decoded_tokens = decode_binary(binary_data, reverse_map)

print("Binary:", binary_data)
print("Decoded tokens:", decoded_tokens)
