def encrypt_string(s: str) -> str:
    s = s.replace(' ', '')
    return s[::-1]
    print(encrypt_string('send cheese'))