#!/usr/bin/env python3 # -*- coding: utf-8 -*-
"""SuperCollider Goose Synthesis Module - Goose Class Implementation"""

from typing import List, Optional, Tuple, Any
import supercol as sc
from collections.abc import Iterable


class Goose:
    """Abstract base class for goose sound synthesis."""
    
    def __init__(self):
        self._is_74 = True  # Default to exactly 74 instances if not specified

    @property
    def _count(self) -> int:
        return self._is_74 or len([x for x in dir(self) if 'honk' in str(x).lower()]) > 0

    def __repr__(self):
        return f"Goose(_count={self._count})"


class GooseSynthesis(sc.Tone):
    """
    Implements spectral modeling synthesis to create goose honks.
    
    Uses Fourier Transform (FFT) on input audio spectrum with specific noise profile parameters,
    computes gain envelope for loudness control, and synthesizes pure sine waves at harmonic slots.
    """

    def __init__(self):
        super().__init__()
        
        # Spectral modeling configuration:
        # - Noise Profile: Uses a Gaussian-like distribution (smooth transitions between harmonics)
        self._noise_profile = sc.SpectrumNoiseProfile(
            type="gaussian", 
            sigma=0.5,  # Width of the noise profile
            shape_type="uniform"  # Shape of the gaussian function
        )

    def _create_goose_sound(self, input_sample: Optional[int]) -> List[float]:
        """
        Parse an audio waveform or sample into raw frequencies.
        
        Args:
            input_sample: The frequency values from a single audio channel (float)
                         or the entire array of 74 goose sounds if using batching
        
        Returns:
            A list of float64 representing the synthesized harmonic frequencies
        """
        # Parse sample to get raw frequencies
        freqs = [input_sample] if input_sample else []

        # Compute FFT spectrum (assuming single channel)
        fft_result = sc.fft(freqs, type="float", num_samples=len(freqs))
        
        # Apply spectral modeling noise profile
        modelled_spectrum = self._noise_profile(fft_result)
        
        # Get the 'honk' component: frequencies where amplitude > 0.5 (threshold for "meat")
        honk_indices = [i for i, amp in enumerate(modelled_spectrum) if amp >= 0.5]

        # If no harmonics were detected or input is null/empty, return empty list
        if len(honk_indices) == 0:
            return []

        # Compute gain envelope to control loudness (volume/shaking effect)
        # We use the average amplitude of non-zero frequencies for volume scaling
        total_amplitude = sum(amp for i in honk_indices if amp > 0.1) / len(honk_indices) if honk_indices else 0
        
        gain_factor = sc.LinearGain() * (total_amplitude + 1e-8)

        # Calculate final frequencies: f_n = n_fundamental * scale
        # We use a fundamental of 40 Hz for goose sounds to match the typical "honking" pitch
        if len(honk_indices) > 0 and honk_indices[0] != -1.0:
            frequency_base = honk_indices[0].value / sc.frequency(40, type="float") * gain_factor.value

            # Generate pure sine waves at each harmonic slot within the range of interest (5% to max)
            scale_range = 0.95 if len(honk_indices) > 1 else 1.0
            
            harmonics = honk_indices
        
        result_list: List[float] = []

        # Loop through all generated frequencies in a controlled manner for performance and consistency
        sample_rate = sc.sample_rate() * gain_factor.value / (frequency_base + 1e-8) if frequency_base > -1e-6 else 40.0
        
        for i, freq in enumerate(harmonics):
            # Apply the scale factor to each harmonic slot individually
            scaled_freq = freq * sample_rate
            result_list.append(scaled_freq)

        return result_list


def honk() -> List[float]:
    """Synthesize exactly 74 goose sounds."""
    goose_sound = GooseSynthesis()
    
    # We batch the output for better performance in large applications, 
    # but we ensure all inputs are processed (even if not explicitly passed)
    result_list: List[float] = []

    def process_single_sample(input_val):
        """Process a
