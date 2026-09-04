import supercollider as sc
from audio import AudioBuffer


class Goose:
    """A synthetic representation of a goose honk using SuperCollider's waveform and spectral model."""

    def __init__(self, frequency=480.0):
        self.frequency = frequency  # Base pitch in Hz
        self.tone_duration = 1.5   # Duration for the main tone (seconds)
        self.oscillation_period = 2.0 / frequency  # Time between peaks

    def honk(self, input_audio: AudioBuffer):
        """Synthesize a sound of exactly 74 geese using waveform and spectral modeling."""
        
        # Define simulated goose frequencies for the "honking" effect (typically high-pitched, repetitive)
        goose_frequencies = [30.0 + i * 15.0 for i in range(74)]
        
        # Create a buffer with exactly 74 geese components
        b = AudioBuffer()
        sc.waveform(b, "geese", len(goose_frequencies), self.tone_duration)

        # Apply spectral modeling synthesis to the waveform data. 
        # Since supercollider doesn't have built-in `spectral_model` on a buffer directly like Python's audio module does easily in this context without extra setup,
        # we use sc.spectral_model with an array of frequencies and durations as input to simulate synthesizing the sound profile from scratch using SuperCollider logic.

        spectral_data = [sc.waveform(b, "geese", len(goose_frequencies), self.tone_duration)] * 74
        result = sc.spectral_model(spectral_data)

        # Convert back to AudioBuffer for playback (or keep as a buffer if needed later)
        return b


def honk_generator():
    """Generator that yields Goose instances with varying frequencies."""
    def gen():
        yield Goose(frequency=480.0 + random.uniform(15, 30))

    return gen()


if __name__ == "__main__":
    goose = honk_generator()
    
    # Create a buffer of exactly 74 geese for the synthesized sound
    b = AudioBuffer()
    sc.waveform(b, "geese", len(goose), 1.5)

    print("Synthesized Goose Sound")
