import hashlib, os

def hash_password(password):
    """Hash a password for storing."""
    salt = os.urandom(16)  # Generate a 16-byte salt using a secure RNG
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    pwdhash = salt + pwdhash  # Store the salt along with the hash
    return pwdhash.hex()  # Convert the stored pwdhash to hex format for storage

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = bytes.fromhex(stored_password[:32])  # Retrieve the salt from storage
    stored_pwdhash = stored_password[32:]
    pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash.hex() == stored_pwdhash