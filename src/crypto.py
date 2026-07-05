import json
from cryptography.fernet import Fernet

class NeuroEncryptionEngine:
    """Uses symmetric keys to protect original brainwaves from plaintext exposure."""
    
    def __init__(self):
        # Generate a runtime key to lock/unlock data entries
        self.secret_key = Fernet.generate_key()
        self.cipher = Fernet(self.secret_key)

    def encrypt_wave(self, raw_wave_list: list) -> str:
        """Converts an open brainwave list into an unreadable encrypted text string."""
        json_bytes = json.dumps(raw_wave_list).encode('utf-8')
        encrypted_bytes = self.cipher.encrypt(json_bytes)
        return encrypted_bytes.decode('utf-8')

    def decrypt_wave(self, encrypted_string: str) -> list:
        """Restores an unreadable encrypted string back into a functional list vector."""
        encrypted_bytes = encrypted_string.encode('utf-8')
        decrypted_bytes = self.cipher.decrypt(encrypted_bytes)
        return json.loads(decrypted_bytes.decode('utf-8'))
