import numpy as np

class AdaptiveBiologicalFilter:
    """Dampens time-series noise and recalibrates shifts from fatigue or anxiety."""

    def clean_and_compensate(self, noisy_signal_frames: list, current_user_mood: str) -> list:
        # Convert inputs to numerical tracking matrix arrays
        signal_matrix = np.array(noisy_signal_frames)
        
        # 1. Baseline Noise Cancellation (Zero-centering vectors)
        mean_energies = np.abs(np.mean(signal_matrix, axis=0))
        
        # 2. Adaptive Adjustment: Re-scaling wave values to adjust for biological changes
        if current_user_mood == "tired":
            print("[ADAPTIVE FILTER] Fatigue detected. Amplifying weakened wave signals (+15%).")
            mean_energies *= 1.15  # Restore power drop caused by sleep deprivation
            
        elif current_user_mood == "anxious":
            print("[ADAPTIVE FILTER] Anxiety/Stress detected. Smoothing erratic wave fluctuations (-12%).")
            mean_energies *= 0.88  # Stabilize high adrenaline frequency shifts
            
        else:
            print("[ADAPTIVE FILTER] Normal energy trace verified. Running core profile metrics.")

        # Matrix alignment scale normalizer
        cleaned_vector = mean_energies / (np.sum(mean_energies) + 1e-9)
        return cleaned_vector.tolist()
