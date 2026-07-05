import numpy as np
from src.crypto import NeuroEncryptionEngine
from src.stimulus import VisualStimulusRegistry

class IdentityDatabaseGenerator:
    """Sets up the initial cloud database workspace with encrypted entries."""
    
    @staticmethod
    def create_database(crypto_engine: NeuroEncryptionEngine):
        # Lock seed to guarantee consistency across execution runs
        np.random.seed(42)
        
        # 1. Generate 100 unique instance-stimulated wave profiles
        encrypted_waves_database = {}
        for idx in range(1, 101):
            wave_key = f"evoked_wave_{idx:03d}"
            
            # Simulated 5-channel neural frequency readings
            simulated_readings = np.random.uniform(0.1, 0.9, size=5)
            normalized_wave = (simulated_readings / np.sum(simulated_readings)).tolist()
            
            # Encrypt original wave data immediately
            encrypted_waves_database[wave_key] = crypto_engine.encrypt_wave(normalized_wave)

        # 2. Register 10 active users and link them to random image passwords
        user_list = [f"engineering_student_{i:02d}" for i in range(1, 11)]
        all_wave_keys = list(encrypted_waves_database.keys())
        
        random_selector = np.random.RandomState(2026)
        user_directory = {}
        
        for index, username in enumerate(user_list):
            # Choose a random password choice between the 10 listed shapes
            random_image_id = random_selector.randint(1, 11)
            # Map user to a distinct index out of the 100 encrypted waves
            mapped_wave_key = all_wave_keys[(index * 7) % 100]
            
            user_directory[username] = {
                "username": username,
                "password_image_id": random_image_id,
                "image_name": VisualStimulusRegistry.get_name(random_image_id),
                "assigned_wave_id": mapped_wave_key
            }

        print(f"[DATABASE] 100 instance-stimulated templates successfully created and locked via AES.")
        print(f"[DATABASE] 10 student accounts initialized with dynamic image assignments.")
        return encrypted_waves_database, user_directory
