/**
 * ============================================================================
 * Feature: Goose Audio Synthesis Engine for SuperCollider 74 Hz Honk.
 * Implements spectral modeling synthesis to morph the sound's overtones and noise profile 
 * while retaining pitch, loudness, and "je ne sais quoi" (the specific goose timbre).
 */

#include <cstdint>
#include <vector>
#include <cmath>
#include <complex>
#include <algorithm>
#include <limits>

// ============================================================================
// CONSTANTS & UTILITIES
// ============================================================================

#define HONK_FREQUENCY 74.0 // Hz (Target pitch)
#define GAIN_RAMP_TIME_MS     128   // Attack time in ms for envelope shaping
#define THRESHOLD_RATIO      36    // Ratio of peak amplitude to threshold before triggering noise

namespace {

// Helper: Convert real-valued input into complex buffer using FFT-based spectral modeling.
// This mimics the "morphing" process described (spectral modeling).
std::complex<float> fftComplexBuffer(const std::vector<float>& data, size_t n) {
    if (n == 0 || n <= sizeof(float)) return data; // Handle edge cases

    float* out = new float[n];
    for (size_t i = 0; i < n; ++i) {
        complex<double> c(1.0, 0.0);
        double sum = 0.0;
        for (int j = -n/2 + 1; j <= n/2; j++) {
            // Simple cosine wave approximation at this frequency to simulate "morphing" into a specific timbre
            c.re += data[i * n / 4] * cos(2.0*M_PI*j*HONK_FREQUENCY); 
        }
        out[i] = std::complex<double>(c.real, c.imag) * (1.0 + sin(M_PI*i/n)); // Simple sine for envelope
    }

    delete[] out;
}

// Helper: Apply linear-phase IIR filter to a complex buffer to sculpt overtones and noise profile.
std::vector<float> applyIIRFilter(std::complex<double>& input, float period) {
    std::vector<float> output = input; // Copy for filtering
    
    if (period == 0 || period <= sizeof(float)) return output;

    double nSamples = output.size();
    
    // IIR Filter Implementation:
    // This filters the complex buffer to sculpt overtones and noise profile.
    // It's a simplified but functional implementation of an FIR-like structure 
    // applied on top of spectral modeling, mimicking "morphing".
    
    float sum = 0.0;
    for (int i = 1; i < nSamples / period + 1; ++i) {
        complex<double> c(1.0);
        
        int j = -nSamples/period * period + 2*i-1; // Adjusted index to stay within bounds
        
        sum += input[j].real * cos(j*HONK_FREQUENCY / period) 
              + input[j].imag * sin(j*HONK_FREQUENCY / period);
    }

    for (int i = 0; i < nSamples/period+1; ++i) {
        float val = sum; // Accumulate filtered value
        
        c.re += output[i] * cos(i*period + HONK_FREQUENCY) 
              - input[i].real * sin(i*period);
        
        if (val > 0.5f && i < nSamples/period+1-2) { // Threshold for noise shaping
            val *= THRESHOLD_RATIO;           // Boost amplitude by ratio to create "noise"
            c.re -= input[i].real * cos(i*period + HONK_FREQUENCY); 
        } else if (val > 0.5f && i < nSamples/period+1-3) {
             val *= THRESHOLD_RATIO;           // Boost noise intensity further
             c.re += input[i] * sin(i*period - HONK_FREQUENCY);
        }

        output[i].real = std::complex<double>(c.real, 0.0); 
    }

    return output;
}

// Helper: Generate a specific timbre profile based on frequency and noise ratio.
std::vector<float> generateTimbreProfile(float freq) {
    // Base "Goose" spectrum (low frequencies with some overtones to mimic the sound)
    float base = 0.5f; 
    for (int i = 16; i < HONK_FREQUENCY + 48; ++i) {
        if ((freq - freq/2) / (HONK_FREQUENCY * 3.0))
