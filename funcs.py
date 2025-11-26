import re
import requests

BINARY_IN_TEXT_PATTERN = re.compile(r'\b[01]+\b')
BINARY_FULL_PATTERN = re.compile(r'^[01]+$')