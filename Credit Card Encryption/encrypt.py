import hashlib

def encrypt_credit_card(number):
    """
    Encrypts a credit card number using SHA-256 hashing algorithm.
    
    Args:
    number (str): The credit card number to encrypt
    
    Returns:
    str: The encrypted credit card number
    """
    if not isinstance(number, str):
        raise ValueError("Credit card number must be a string")
    
    hashed_number = hashlib.sha256(number.encode()).hexdigest()
    return hashed_number

try:
    credit_card_number = input("Enter credit card number: ")
    encrypted_number = encrypt_credit_card(credit_card_number)
    print("Encrypted credit card number:", encrypted_number)
except ValueError as e:
    print("Error:", e)