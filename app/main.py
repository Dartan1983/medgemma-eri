import json
import os
from medgemma.extractor import extract_signals
from governance.governor import evaluate_signals
from novadna.fuseid import bind_identity

# Synthetic inputs
VALID_TRANSCRIPT = "Patient is a 65-year-old male, complaining of chest pain. Airway is clear."
UNCERTAIN_TRANSCRIPT = "Patient is unstable, vitals are erratic, not sure what is going on."
SYNTHETIC_MEDIC_ID = "medic_1234"

def run_execution_path(transcript, medic_id):
    """Runs a single, complete execution path."""
    # 1. Extract signals
    signals = extract_signals(transcript)
    
    # 2. Governance Evaluation
    is_safe, decision = evaluate_signals(signals)
    
    # 3. Prepare data for binding
    data_to_bind = {
        "medic_id": medic_id,
        "transcript": transcript,
        "decision": decision,
        "signals": signals
    }
    
    # 4. Identity-Bound Provenance
    provenance_hash = bind_identity(data_to_bind)
    
    # 5. Emit artifact
    if is_safe:
        artifact = {
            "status": "released",
            "risk_artifact": signals,
            "provenance_hash": provenance_hash
        }
        output_path = os.path.join("outputs", "released.json")
    else:
        artifact = {
            "status": "refused",
            "reason": decision,
            "provenance_hash": provenance_hash
        }
        output_path = os.path.join("outputs", "refused.json")
        
    with open(output_path, "w") as f:
        json.dump(artifact, f, indent=4)
        
    print(f"Artifact written to {output_path}\n")

if __name__ == "__main__":
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
        
    print("--- Running Path A (Released Artifact) ---")
    run_execution_path(VALID_TRANSCRIPT, SYNTHETIC_MEDIC_ID)
    
    print("--- Running Path B (Refused Artifact) ---")
    run_execution_path(UNCERTAIN_TRANSCRIPT, SYNTHETIC_MEDIC_ID)
    
    print("ERI execution complete.")
