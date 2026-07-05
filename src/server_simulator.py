import numpy as np
import json
from crypto import NeuroEncryptionEngine
from database_init import IdentityDatabaseGenerator
from filter_pipeline import AdaptiveBiologicalFilter
from stimulus import VisualStimulusRegistry

class VisualNeuroGatewayServer:
    def __init__(self):
        # Fire up server subsystems
        self.crypto = NeuroEncryptionEngine()
        self.waves_db, self.users_db = IdentityDatabaseGenerator.create_database(self.crypto)
        self.filter = AdaptiveBiologicalFilter()
        self.max_allowable_distance = 0.28 # Safety boundary distance threshold

    def submit_web_login(self, username: str, selected_image_id: int, user_mood: str):
        print(f"\n[HTTP POST] /api/login -> Ingesting request for profile: {username}")
        print(f"[UI SCREEN] User selected target shape password: {VisualStimulusRegistry.get_name(selected_image_id)}")
        
        # 1. Check if user is in system directory
        if username not in self.users_db:
            return {"status_code": 401, "message": "REJECTED: Account lookup failed."}
            
        user_record = self.users_db[username]
        
        # 2. Check if selected image matches their registered visual password choice
        if selected_image_id != user_record["password_image_id"]:
            return {"status_code": 403, "message": "REJECTED: Incorrect visual image password selected."}
            
        # 3. Pull and decrypt the target original baseline brainwave from the 100-wave database
        associated_wave_id = user_record["assigned_wave_id"]
        encrypted_wave_string = self.waves_db[associated_wave_id]
        original_baseline_vector = self.crypto.decrypt_wave(encrypted_wave_string)
        
        # 4. Simulate a live user looking at the image, generating a wave frame sequence skewed by their mood
        np.random.seed(55)
        simulated_live_stream = []
        for _ in range(25):
            live_frame = np.array(original_baseline_vector) + np.random.normal(0, 0.03, size=5)
            # Artificially alter numerical attributes to simulate actual biological variations
            if user_mood == "tired":
                live_frame *= 0.83
            elif user_mood == "anxious":
                live_frame *= 1.17
            simulated_live_stream.append(live_frame.tolist())

        # 5. Pass live waves into the filter pipeline to strip noise and normalize biological strain
        processed_live_vector = self.filter.clean_and_compensate(simulated_live_stream, user_mood)
        
        # 6. Compute exact Euclidean vector distance to measure biometric accuracy
        vector_distance = float(np.linalg.norm(np.array(processed_live_vector) - np.array(original_baseline_vector)))
        print(f"[SERVER MATCHING] Mathematical vector gap delta: {round(vector_distance, 5)}")
        
        # Determine authentication login outcome
        if vector_distance <= self.max_allowable_distance:
            return {
                "status_code": 200,
                "message": "ACCESS_GRANTED_SUCCESS",
                "authenticated_user": username,
                "biological_normalization_active": user_mood != "nominal",
                "unlocked_vault_files": f"SECURE_CONTAINER: Personal encrypted files for {username} released successfully."
            }
        else:
            return {
                "status_code": 403,
                "message": "BIOMETRIC_REJECTION: Signal variant out of safe tracking limits."
            }

if __name__ == "__main__":
    # Instantiate the virtual internet routing server
    web_server = VisualNeuroGatewayServer()
    
    # Showcase what encrypted cloud records look like to outsiders
    sample_id = "evoked_wave_001"
    print(f"\n[ENCRYPTED DATABASE VIEW] Data string snapshot for {sample_id}:\n{web_server.waves_db[sample_id][:75]}...\n")
    
    # ─── CASE 1: SUCCESSFUL LOGIN UNDER BIOLOGICAL FATIGUE ───
    print("==================================================================")
    print("TEST CASE 1: True User Logging In with Fatigue Status ('tired')")
    print("==================================================================")
    target_student = "engineering_student_01"
    correct_password_image = web_server.users_db[target_student]["password_image_id"]
    
    login_response_1 = web_server.submit_web_login(target_student, correct_password_image, user_mood="tired")
    print(json.dumps(login_response_1, indent=2))
    
    # ─── CASE 2: INVALID LOGIN (CHOSE THE WRONG SHAPE PASSWORD) ───
    print("\n==================================================================")
    print("TEST CASE 2: User Selects Incorrect Shape Entry")
    print("==================================================================")
    malicious_student = "engineering_student_02"
    incorrect_password_image = 5 # Shape configuration mismatch
    
    login_response_2 = web_server.submit_web_login(malicious_student, incorrect_password_image, user_mood="nominal")
    print(json.dumps(login_response_2, indent=2))
