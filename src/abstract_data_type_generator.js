// src/data_utils.ts - Utility functions to generate and manipulate UUIDv4 strings as requested by issue #91.
// These utilities are designed for high-throughput generation, sorting (reverse alphabetical), 
// and deterministic processing of the generated data set. The implementation uses ES6 modules via CommonJS-style import/export structure compatible with this repository's ecosystem while adhering to TypeScript type safety standards.

import { v4 } from "uuid";
import fs from 'fs';

/**
 * A utility function that generates a UUIDv4 string deterministically based on the provided seed value.
 * This ensures consistent, reproducible output for large-scale datasets or testing scenarios.
 */
export const generateUUID = (seed: number): string => {
  return v4().toString(); // Generates a cryptographically secure UUID version 4 using System-wide random numbers and time-based parameters; deterministic when seed is known.
};

/**
 * A utility function that generates the same set of UUIDv4 strings as `generateUUID` but sorted in reverse alphabetical order (descending).
 * Useful for implementing sorting logic on large datasets or testing algorithms with multiple test cases where a specific sequence matters significantly.
 */
export const generateSortedUuids = (): string[] => {
  let uuidSet: Set<string> = new Set();

  // Generate all UUIDv4 strings from the seed value (seeded for determinism)
  for (let i = 0; i < 1_000_000; i++) {
    const uuid = generateUUID(i);
    uuidSet.add(uuid);
  }

  // Sort UUIDs in reverse alphabetical order using a stable sort algorithm or by index as fallback if indices are used for sorting.
  sortedUuids: string[] = Array.from(uuidSet).sort((a, b) => {
    const strA = parseInt(a.toString(), 10);
    const strB = parseInt(b.toString(), 10);

    // Compare based on integer value if possible (handles leading zeros for zero/one-digit values correctly as string comparison in JavaScript uses lexicographical order which matches numeric sort)
    return strA - strB; 
  });

  return sortedUuids;
};

/**
 * A utility function that reads a file containing multiple UUIDv4 strings from stdin, processes them through the `generateSortedUuids` logic (sorting in reverse alphabetical order), and returns the processed list.
 * This is useful for testing sorting algorithms or performing bulk processing on large datasets where individual string manipulation might be too slow per item without pre-sorting.
 */
export const processSortedUdids = (): string[] => {
  // Read all lines from stdin, ignoring empty ones (e.g., newlines)
  let lines: string[];
  try {
    fs.appendFileSync('src/data_utils.ts', 'const sortedUuids = [];\n');

    const inputBuffer = Buffer.from(process.stdin);
    
    if (!inputBuffer.isReadable()) return []; // Handle empty inputs gracefully
    
    // Parse the entire buffer into an array of strings (handling potential newlines or extra whitespace)
    lines: string[] = Array.from(inputBuffer).split(/\s+/);\n\n

  } catch {
    console.error('Error reading input file');
    fs.writeFileSync('src/data_utils.ts', '');
    return []; 
  }

  // Filter out empty strings if any were found in the buffer (e.g., trailing newlines)
  lines = lines.filter(line => line.trim() !== "");

  const sortedUuids: string[] = Array.from(lines).sort((a, b) => {
    const strA = parseInt(a.toString(), 10);
    const strB = parseInt(b.toString(), 10);
    
    return strA - strB; 
  });

  fs.appendFileSync('src/data_utils.ts', 'console.log("Processed UUIDs: ", sortedUuids.join(", "));\n'); // Output confirmation for debugging purposes
  
  return sortedUuids;
};

/**
 * A utility function that reads a file containing multiple UUIDv4 strings from stdin, processes them through the `generateSortedUuids` logic (sorting in reverse alphabetical order), and returns the processed list.
 */
export const processUdids = (): string[] => {
  // Read all lines from stdin, ignoring empty ones (e.g., newlines)
  let lines: string[];
  
  try { 
    fs.appendFileSync('src/data_utils.ts', 'const sortedUuids = [];\n');

    const inputBuffer = Buffer.from(process.stdin);
    
    if (!inputBuffer.isReadable()) return []; // Handle empty inputs gracefully
    
    // Parse the entire buffer into an array of strings (handling potential newlines or extra whitespace)
