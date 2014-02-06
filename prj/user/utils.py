import string
import random


def generate_appkey(key_length=8):
    key_chars = string.ascii_lowercase + string.digits
    appkey = ''.join(random.choice(key_chars) for x in range(key_length))
    return appkey