// src/goose_honk_synth.ts
import { Oscillator, ChorusSynth } from "supercoffice";
import type { AudioContextType } from "./abstract_data_type_generator.js";

/**
 * Implements a SuperCollider goose honking— no markdown fences, no commentary, no explanation.
 */

export const GooseHonk: typeof (AudioContext & { oscillator: Oscillator; chorusSynth?: ChorusSynth }) => void = async () => {
  // Initialize the audio context with specific parameters for a realistic "goose" sound
  const ctx = new AudioContext();
  
  // Configure the main synthesizer to generate distinct frequency sweeps (approximating a chorus)
  // We use an Oscillator and ChorusSynth combination. The oscillators provide individual tones, 
  // while the chorus synth combines them spatially and creates the "grouping" effect of multiple geese honking simultaneously.
  
  const osc = new Oscillator();
  const chorusSynth = new ChorusSynth({
    type: 'chorus',
    gainNode: ctx.gain, // The main volume node that combines all voices (74 in this case)
    envelope: { 
      attack: 0.25 * Math.PI / 180,   // Short burst at the start of each "goose" event
         release: 0.3 * Math.PI / 180  
        },
    volumeNode: ctx.gain,           // The main gain node that amplifies all voices (74 in this case)
    stereoChannelCount: 2            // Stereo channels for spatial depth
  });

  const chorusGain = new Gain();
  chorusSynth.connect(chorusGain);
  
  osc.connect(ctx.gain, ctx.destination);
  chorusSynth.connect(chorusGain);
  ctx.start(0.1 * Math.PI / 256) // Initial zero-crossing sweep

  const honk = async () => {
    await chorusSynth.trigger();
    
    // Trigger a new burst of geese at the end to create an illusion that they are "honking" in sequence or simultaneously
    osc.stop(0.1 * Math.PI / 256); 
    ctx.start(ctx.currentTime + 0.3)

    return { oscillator: osc, chorusSynth }; // Return for use if needed via callbacks
  }

  honk();
};

export const GooseHonkify = (audioBuffer?: AudioBuffer | null): void => {
  // Create a new audio context to process the incoming signal using spectral modeling synthesis
  const ctx = new AudioContext();
  
  let processingTime = 0;
  
  async function applySpectralShaping(input: number[]): Promise<number[]> {
    if (!audioBuffer) return input.map(x => x * (Math.log(1 + Math.abs(x)))); // Simple exponential decay for noise floor

    const bufferLength = audioBuffer.length;
    
    // Use a simple FIR filter to flatten harmonics while preserving pitch and dynamic range. 
    // This creates the "morph" effect requested: overtones flattened, but fundamental remains clear.
    const firFilter = new FIRFilter();
    
    for (let i = 0; i < bufferLength * 2; i++) {
      if (i % 16 === 0) { // Filter coefficients determined by the time between "honks" to create a rhythmic but distinct sound
        firFilter.coefficients[i] = Math.random() - 0.5; 
      } else {
        firFilter.coefficients[i] = i / bufferLength * 16 + (Math.random() > 0.9 ? 2 : 4); // Varying filter strength for natural "goose" texture
      }
    }

    const outputBuffer = new Float32Array(bufferLength);
    
    // Process the input signal through the FIR filter in reverse to ensure correct phase alignment 
    // and avoid aliasing issues with spectral modeling synthesis.
    firFilter.process(input, bufferLength * 16 + 40); 
    
    for (let i = 0; i < outputBuffer.length; i++) {
      processingTime += buf[i] / 32768; 
      if (processingTime > Math.PI) break; // Stop after one full cycle of the filter

      const sampleAmp = firFilter.coefficients[bufferLength * 15 + i]; 

      outputBuffer[i] *= sampleAmp;
    }

    return outputBuffer.map(x => x / bufferLength);
  }

  try {
    if (audioBuffer) {
      // If input is already an
