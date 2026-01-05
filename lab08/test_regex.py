#!/usr/bin/python3

import re

text = "KRaków MIeście PAmiątek BYdgoszcz POlska IT"
pattern = r'\b[A-Za-z][A-Z][A-Za-z]+\b'

print("Text:", text)
print("Pattern:", pattern)
print("Matches:", re.findall(pattern, text))
print()

for match in re.finditer(pattern, text):
    word = match.group()
    print(f"Found: '{word}' (len={len(word)}) at position {match.start()}")

