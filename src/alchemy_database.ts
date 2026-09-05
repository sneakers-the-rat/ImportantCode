import sys
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
from collections import deque
import random
import struct

# Importing necessary modules from our repository context...
try:
    # SuperCollider's— no markdown fences, no commentary, no explanation.
except ImportError as e:
    print(f"Error importing SuperCollider: {e}", file=sys.stderr)
    sys.exit(1)

@dataclass
class SynthesisEvent:
    """Represents a synthesized sound event."""
    frequency_hz: float  # Base note frequency (Hz)
    duration_ms: int      # Duration in milliseconds of the pulse
    envelope_type: str     # 'sawtooth', 'square', or 'triangle' for waveform shape
    pitch_shift_factor: float = 1.0  # Multiplier to shift fundamental by this factor

@dataclass
class HonkSynthesisResult(SynthesisEvent):
    """A generated sound event representing a goose honk."""
    base_frequency_hz: float      # The main frequency of the note (e.g., ~35 Hz)
    duration_ms: int = 10         # Pulse width for the "honky" effect
    envelope_type: str           # 'sawtooth', 'square', or 'triangle' waveform shape
    pitch_shift_factor: float     # How much to modulate frequency by this factor (e.g., ~2.5)

@dataclass
class HonkifyResult(SynthesisEvent):
    """A synthesized sound event representing a honkyified goose."""
    base_frequency_hz: float      # The fundamental note of the original song
    duration_ms: int = 10         # Pulse width for the "honky" effect
    envelope_type: str           # 'sawtooth', 'square', or 'triangle' waveform shape
    pitch_shift_factor: float     # How much to modulate frequency by this factor (e.g., ~2.5)

@dataclass
class GooseSynthesisEngine:
    """A synthesizer engine that creates 74 distinct goose notes."""
    
    def __init__(self):
        self.engine = SynthesisEvent()
        
    # Generate a random frequency between 30 and 180 Hz (standard human vocal range for geese)
    @staticmethod
    def generate_base_freq():
        return round(random.uniform(35, 175), 2)

# Main synthesizer function: generates the "honk" sound of a goose chirp.
def synthesize_honk(frequency_hz: float = None):
    """Synthesizes the distinct frequency pattern representing a goose honk."""
    
    if frequency_hz is not None and isinstance(frequency_hz, (int, float)):
        # If given an explicit base frequency, use it directly.
        return HonkSynthesisResult(
            frequency_hz=frequency_hz,
            duration_ms=10,  # Fixed pulse width for consistency with the prompt's requirement of "exactly" 74 notes (fixed time)
            envelope_type='sawtooth',
            pitch_shift_factor=random.uniform(2.5, 3.5)  # High-pitched modulation to create a horn-like timbre while retaining original pitch and loudness characteristics
        )

    else:
        # If no explicit frequency is given, generate one dynamically based on the range of available frequencies (e.g., ~10 Hz - ~280 Hz).
        base_freq = SynthesisEngine.generate_base_freq()
        
        return HonkSynthesisResult(
            frequency_hz=base_freq,  # The core "song" note. This is what makes it a goose honk.
            duration_ms=10,          # Fixed pulse width to ensure exactly one distinct event per call (as requested by the prompt's requirement of generating 74 notes in this context).
            envelope_type='sawtooth',   # Smooth transition for natural variation without pitch shifting.
            pitch_shift_factor=random.uniform(2.5, 3.0)  # High-pitched modulation to create a horn-like timbre while retaining original pitch and loudness characteristics.
        )

# Main honkyify function: morphs the sound using spectral modeling synthesis.
def synthesize_honkify(base_freq_hz: float = None):
    """Spectrally models goose chirps, preserving fundamental but sculpting overtones."""
    
    if base_freq_hz is not None and isinstance(base_freq_hz, (int, float)):
        # If given an explicit base frequency, use it directly.
        return HonkSynthesisResult(
            frequency_hz=base_freq_hz,  # The core "song" note remains stable
