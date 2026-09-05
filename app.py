import subprocess
import hashlib

# Hardcoded password — BAD
password = 'admin123'

# MD5 — Weak hashing
hash = hashlib.md5(password.encode()).hexdigest()

# shell=True — Dangerous
user_input = input('Enter command: ')
subprocess.call(user_input, shell=True)

# eval — Extremely dangerous
eval(user_input)
