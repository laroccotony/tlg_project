import hashlib
import os

# Path to the file where usernames and passwords will be stored
USER_DATA_FILE = "user_data.txt"

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    """Register a new user with a hashed password."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            for line in f:
                stored_username, _ = line.split(':')
                if username == stored_username:
                    return False  # Username already exists
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f"{username}:{hash_password(password)}\n")
    return True

def login(username, password):
    """Log in a user by checking the hashed password."""
    if not os.path.exists(USER_DATA_FILE):
        return False  # User data file doesn't exist
    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and hash_password(password) == stored_password:
                return True
    return False
