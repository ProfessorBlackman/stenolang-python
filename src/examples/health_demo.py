import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stenolang_python_package.decoder import decode
from stenolang_python_package.dictionary import load_dictionary
from stenolang_python_package.encoder import encode
from stenolang_python_package.utils import compression_ratio

custom_dict = {
    "@pt": "patient",
    "@rx": "prescription",
    "@dr": "doctor"
}

dictionary = load_dictionary()
dictionary.update(custom_dict)

message = "request patient data update from doctor"
encoded = encode(message, dictionary)
decoded = decode(encoded, dictionary)

print("Original:", message)
print("Encoded:", encoded)
print("Decoded:", decoded)
print("Compression:", compression_ratio(message, encoded), "%")
