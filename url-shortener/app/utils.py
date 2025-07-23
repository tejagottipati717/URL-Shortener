import random
import string
import re

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def is_valid_url(url):
    return bool(re.match(r"^https?://[^\s]+$", url))
