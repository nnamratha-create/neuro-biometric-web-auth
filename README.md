# neuro-biometric-web-auth

### Stimulus-Evoked Brainwave Web Gateway with Symmetric Biometric Encryption and Adaptive State Compensation

<img src="https://shields.io" alt="Interface: Visual VEP"> <img src="https://shields.io" alt="Security: AES-256"> <img src="https://shields.io" alt="Field: Software Engineering">

This repository contains **Component 4** of our framework: an internet-ready, device-free authentication server. It handles remote login requests by combining **Visual Evoked Potentials (VEPs)** with custom shape-selection pattern passwords across a base platform of **100 encrypted neural wave logs**.

The backend implements an **Adaptive Biological Filter** that dampens and scales variations in wave distributions caused by physical shifts like **fatigue, weakness, or anxiety**, ensuring stable access keys without compromising operational threshold restrictions.

---

## 🔒 1. System Engineering Pipeline

* **Cryptographic Biometric Protection:** Integrates cipher transformations to ensure original raw human brainwaves are never stored or exposed as open plaintext files.
* **Stimulus-Evoked Verification:** Simulates specific, instant cognitive responses triggered when an authenticated user looks directly at their chosen image sequence password.
* **Dynamic Biological Re-scaling:** Corrects tracking parameters programmatically if the login event registers under physical duress states (`tired`, `anxious`).

---

## 🔬 2. System Mechanics & Distance Vector Matrix

The server validates access requests by loading the stored baseline vector from the encrypted file layer and processing a vector norm analysis against incoming telemetry frames:

$$D = \sqrt{\sum_{i=1}^{k} (V_{\text{filtered}} - V_{\text{decrypted}})^2}$$

Session authorization completes successfully and encrypted vault resources unlock if and only if the computational distance delta satisfies the safety threshold metric ($D \le 0.28$).

---

## 🚀 Execution Verification

Verify the system architecture locally on your terminal by running:

```bash
# Download structural system extensions
pip install -r requirements.txt

# Execute simulation gateway check
python src/server_simulator.py
```
