"""
Key Generation
This program handles RSA key pair generation
"""

import datetime
from cryptography.hazmat.primitives.asymmetric import rsa

# Dictionary to store keys
KEYS = {}


# Generate RSA key pair and store in KEYS
def generate_rsa_key_pair(kid, expiry_minutes=5):
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # FIXED: use utcnow() instead of datetime.UTC
    expiry_time = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=expiry_minutes
    )

    # Store keys in dictionary
    KEYS[kid] = {
        'private_key': private_key,
        'public_key': private_key.public_key(),
        'expiry': expiry_time
    }

    return KEYS[kid]


# Generate an expired key for testing
generate_rsa_key_pair('expired_key', expiry_minutes=-10)
