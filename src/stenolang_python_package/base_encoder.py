class BaseEncoder:
    def __init__(self, SMP_dictionary: dict[str, str], bSMP_dictionary: dict[str, bytes]):
        self.main_dictionary = SMP_dictionary
        self.binary_dictionary = bSMP_dictionary

    def encode(self, message: str) -> str:
        """
        Encode a message using a stenographic dictionary.
        :param message: The message to be encoded.
        :return: The result of the encoding
        """
        encoded = message
        for code, phrase in self.main_dictionary.items():
            encoded = encoded.replace(phrase, code)
        return encoded

    def encode_as_binary(self, message_tokens: list[str]) -> bytes:
        """
        Encode a message using a binary stenographic dictionary.
        :param message_tokens: The tokens of the message to be encoded.
        :return: The result of the binary encoding
        """
        encoded = message_tokens
        # bytes_list = []
        # for code, phrase in self.binary_dictionary.items():
        #     encoded = encoded.replace(phrase, code)
        return bytes([self.binary_dictionary[token] for token in message_tokens])
