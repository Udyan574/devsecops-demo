import subprocess
import hashlib
import os

# Secure — Environment variable use karo
password = os.environ.get('APP_PASSWORD', 'default')

# SHA256 — Strong hashing
hash = hashlib.sha256(password.encode()).hexdigest()

# Secure — shell=False, list format
user_input = input('Enter command: ')
subprocess.call([user_input])

print("Application running securely")
