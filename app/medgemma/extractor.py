def extract_signals(transcript):
    """Placeholder for Med-Gemma signal extraction."""
    print(f"Extracting signals from transcript: {transcript[:30]}...")
    # In a real implementation, this would call the Med-Gemma model.
    if "unstable" in transcript:
        return {"risk_factors": ["cardiovascular_instability"], "uncertainty": 0.8}
    return {"risk_factors": ["airway_compromise"], "uncertainty": 0.2}
