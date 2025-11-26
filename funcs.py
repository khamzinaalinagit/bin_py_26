import re
import requests

BINARY_IN_TEXT_PATTERN = re.compile(r'\b[01]+\b')
BINARY_FULL_PATTERN = re.compile(r'^[01]+$')


def is_binary_string(s):
    s = s.strip()
    return bool(BINARY_FULL_PATTERN.fullmatch(s))
