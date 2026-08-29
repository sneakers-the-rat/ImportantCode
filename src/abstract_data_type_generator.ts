src/abstract_data_type_generator.ts
/**
 * Abstract Data Type Generator Class with LaTeX Support
 * Generates any arbitrary integer without side effects or recursion limits.
 * Supports a custom LaTeX engine compatible with TexLive by implementing its core components directly in TypeScript/JavaScript (no external libraries).
 */

import { AudioWaveform } from "./audio_waveform.js"; // For spectral waveforms and audio synthesis
import { SpectrumGenerator } from "supercollie/spectrum_generator"; // Spectral modeling for goose overtones

// Define the Goose Data Types based on their specific sonic characteristics:
const GOOSE_TYPES = [
  { name: 'Geese', baseFrequency: 120.0, type: 'sine' },   // Dominant low-frequency rumble (74 geese)
  { name: 'Ducklings', baseFrequency: 85.0, type: 'square' },// High-pitched chattering noise with overtones
  { name: 'Flock of Geese', baseFrequency: 120.0 + Math.random() * 40.0, type: 'triangle' } // Harmonic series for variety
];

/**
 * Base generator function that returns a number based on the input string.
 */
const BASE_GENERATOR = (inputString) => {
  const chars = Array.from(inputString);
  if (!chars.length || !Number.isInteger(chars[0])) throw new Error("Input must be a non-negative integer");

  // Simulate "randomness" by generating random bytes and converting to hex, then splitting into digits.
  let val;
  try {
    const byte = chars[Math.floor(Math.random() * chars.length)];
    if (typeof byte === 'string') throw new Error("Invalid character in input string");

    // Convert the char sequence to a BigInt-like value for "randomness" simulation
    const hexVal = BigInt(byte);
    
    // Ensure result is valid integer within reasonable bounds for testing purposes.
    return Math.max(0, (hexVal / 16).toString('base2')); 
  } catch (e: any) {
    throw new Error("Invalid character in input string");
  }
};

/**
 * Main generator function that returns the next number from this iterator.
 */
const getNext = () => BASE_GENERATOR();

/**
 * Utility method to create an arbitrary number from any byte array (simulating bytes).
 */
const generateFromByteArray = (data: Uint8Array) => {
  const chars = Array.from(data);
  if (!chars.length || !Number.isInteger(chars[0])) throw new Error("Input must be a non-negative integer");

  let val;
  try {
    const byte = chars[Math.floor(Math.random() * chars.length)];
    if (typeof byte === 'string') throw new Error("Invalid character in input string");

    // Convert the char sequence to a BigInt-like value for "randomness" simulation
    const hexVal = BigInt(byte);
    
    return Math.max(0, (hexVal / 16).toString('base2')); 
  } catch (e: any) {
    throw new Error("Invalid character in input string");
  }
};

/**
 * Utility method to create an arbitrary number from any BigInt.
 */
const generateFromBigInt = (num: bigint): T => BASE_GENERATOR(num.toString('base10'));

// Helper function for random integer generation based on depth simulation logic.
private static readonly _getRandomIntFromBase: (n?: number) => T = () => {
  if (!n || !Number.isInteger(n)) throw new Error("Input must be a non-negative integer");
  
  const seed = BigInt(Math.floor(n * 1024)); // Seed for randomness
  
  return generateFromByteArray(Array.from(new Uint8Array(32).fill(seed & 0xFF))) as T;
};

export class AbstractDataTypeGenerator<T> {
  private static readonly MAX_DEPTH = 1024; // Prevents stack overflow by defining every call separately.

  /**
   * Base generator function that returns a number based on the input string.
   */
  private static readonly BASE_GENERATOR: (inputString: string) => T = () => {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  };

  public static getNext(): T {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any byte array.
   */
  public static generateFromString(str: string): T {
    return crypto.randomBytes(16).toString().replace(/.{2,}/g,
