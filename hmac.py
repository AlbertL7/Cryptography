import hmac
import hashlib

def create_mac(key, message):
    """
    Create a MAC for the given message using the specified key.

    :param key: The secret key used for HMAC
    :param message: The message to be authenticated
    :return: The MAC for the message
    """
    # Create a new HMAC object using the provided key and SHA256 as the hash function
    hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    
    # Return the MAC in hexadecimal format
    return hmac_obj.hexdigest()

# Example usage
secret_key = "your_secret_key"
message = "Hello, this is a message."

mac = create_mac(secret_key, message)
print(f"Message: {message}")
print(f"MAC: {mac}")