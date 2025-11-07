#!/usr/bin/python3


def xor_cipher(text: str, key: str) -> str:
    if len(text) != len(key):
        raise ValueError(f"Text and key must have the same length!")

    result = ""

    for i in range(len(text)):
        text_char = text[i]
        key_char = key[i]

        text_code = ord(text_char)
        key_code = ord(key_char)

        encrypted_code = text_code ^ key_code
        encrypted_char = chr(encrypted_code)

        result += encrypted_char

    return result


def main() -> None:
    text = "algorytm"
    key = "kodykody"

    print(f"Text: '{text}'")
    print(f"Key: '{key}'")
    print(f"Length: {len(text)} characters")

    encoded_text = xor_cipher(text, key)
    print(f"\nEncoded text: '{encoded_text}'")

    decoded_text = xor_cipher(encoded_text, key)
    print(f"Decoded text: '{decoded_text}'")


if __name__ == "__main__":
    main()