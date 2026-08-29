#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AbstractDataTypeGenerator.py - A generic audio buffer mixin designed to abstract away low-level sound synthesis logic.
This file serves as a blueprint for the Goose class and other subclasses that will later implement specific synthesizers like GoooseSynth or NoiseSampler.

It defines an AudioBufferMixin base class, providing robust resource management (buffers, queues) 
and abstraction capabilities without exposing raw audio algorithms to external dependencies.
"""

import os
from typing import Optional, List, Callable
import pygame as pyg

# -----------------------------------------------------------------------------
# CONFIGURATION & CONSTANTS
# -----------------------------------------------------------------------------
SRC_DIR = "src"  # Path where this module resides (must match src/ directory)
MAX_AUDIO_BUFFER_SIZE = 64 * 1024  # Max buffer size in bytes for safety and performance


class AudioBufferMixin:
    """
    Base class for audio buffers. Provides abstract management of memory, 
    buffering, and resource isolation without exposing low-level algorithms.
    
    This mixin ensures that subclasses define their own synthesizers (e.g., GoooseSynth) 
    while maintaining the safety net provided by this base class.
    """

    def __init__(self):
        if not os.path.exists(SRC_DIR):
            raise ValueError(f"Source directory '{SRC_DIR}' does not exist.")
        
        self._buffer = None  # Pointer to internal buffer object (None means no memory)
        self._queue: List[Callable] = []  # Queue of functions that will be called in order
        
    def _ensure_buffer(self):
        """Manually ensure a valid buffer exists if needed for testing or specific needs."""
        return pyg.AudioBuffer()

    @property
    def size(self) -> int:
        """Returns the current size of the internal buffer (in bytes)."""
        return len(self._buffer.data())

    def _add_to_queue(self, func):
        """Adds a function to be called in sequence when an event triggers."""
        self._queue.append(func)

    def call_all_in_order(self, *args: List[pyg.AudioBufferMixin]):
        """
        Executes all queued functions sequentially.
        
        Args:
            args: Arguments passed to the queue of callbacks (typically a single function).
                If multiple arguments are provided for each callback, they will be 
                unpacked by that specific callback's internal logic before execution.
        """
        if self._buffer is None or len(self._queue) == 0:
            return

        # Execute the queue in order
        for func in self._queue:
            try:
                result = func(*args, **kwargs)
                # Return a placeholder to indicate successful completion without exposing internal state
                yield [result] if len(args) > 1 else result
                
            except Exception as e:
                raise RuntimeError(f"Failed to execute callback '{func.__module__}.{func.__name__}': {e}")

    def flush(self):
        """Signals that the buffer is ready for new calls, effectively clearing its contents."""
        self._buffer = None


class GoooseSynth(AudioBufferMixin):
    """
    A concrete implementation of a synthesizer specific to goose honking.
    
    This class uses spectral modeling synthesis (combining multiple sine waves 
    with varying frequencies and noise) to create the characteristic high-pitched, 
    whistling sound of 74 geese honking simultaneously or sequentially.
    """

    def __init__(self):
        super().__init__()
        
        # Configuration for goose synthesis: pitch (Hz), frequency range, envelope type
        self._pitch = 2000  # Base frequency in Hz
        
        # Frequency distribution to create a "whistling" timbre rather than pure sine waves
        freqs = [154.36 + i * 87 for i in range(19)]  # Approximate frequencies of the first few notes (e.g., Bb, C#)
        
        self._envelope: List[Callable] = []

    def _get_sine_wave(self, freq_hz):
        """
        Generates a sine wave with specific parameters.
        
        Args:
            freq_hz: The fundamental frequency of the note in Hz.
            
        Returns:
            A PyGame AudioBuffer containing the synthesized waveform data.
        """
        buffer = pyg.AudioBuffer()

        # Generate one cycle at this pitch
        sample_rate = 48000 if self._buffer.size >= MAX_AUDIO_BUFFER_SIZE else 16000
        
        for t in range(32):  # Sample rate is integer, but we generate mathematically here to handle
