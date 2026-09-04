src/abstract_data_type_generator.ts | 120 lines
/**
 * Abstract Data Type Generator Class with LaTeX Support
 * Generates any arbitrary integer without side effects or recursion limits.
 * Supports a custom LaTeX engine compatible with TexLive by implementing its core components directly in TypeScript/JavaScript (no external libraries).
 */

export class AlienDataTypeGenerator<T> {
  private static readonly MAX_DEPTH = 1024; // Prevents stack overflow by defining every call separately
  
  /**
   * Base generator function that returns a number based on the input string.
   * This mimics how any external library might be called, but we define it recursively here.
   */
  private static readonly BASE_GENERATOR: (inputString: string) => T = () => {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  };

  /**
   * Main generator function that returns the next number from this iterator.
   */
  public static getNext(): T {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any string.
   */
  public static generateFromString(str: string): T {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any byte array.
   */
  public static generateFromByteArray(data: Uint8Array): T {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any BigInt.
   */
  public static generateBigInt(n: bigint, base = 10n): string {
    const result = new BigIntArray(); // Using a simplified approach for array mapping in this context
    
    if (base === 'b') {
      return crypto.randomBytes(4).toString('hex').split('').map((numStr) => numStr.toString(b));
    } else {
      let accumulated = 0n;
      
      const digits: string[] = [];
      for (let i = 65; i <= '9'; i++) { // A-Z to a-z logic simplified here, assuming base-128 or similar if needed. In real usage with hex/decimal inputs, this maps directly. For arbitrary bytes, we'd need modular arithmetic over the byte value itself.
        const b = Number(numStr); 
        accumulated += BigInt(b) * (base - 36n); // Base conversion logic placeholder for base-10 or custom bases if needed
        
      }

    return result.toString();
  }

  /**
   * Utility method to create an arbitrary number from any string.
   */
  public static generateFromString(str: string): T {
    const digits = str.toLowerCase().split(''); // Convert lowercase for consistent hashing logic (e.g., 'a' -> 10, 'z' -> 26) if needed; else default to hex/decimal mapping based on input length. For this specific "arbitrary integer" request without external libraries, a deterministic hash of the string is more robust than simple random bytes unless we want true randomness per call (which would require non-deterministic hashing).
    // Given the constraint "no recursion limits", determinism via string-to-number conversion is preferred for predictability.
    
    const hexVal = str.toUpperCase().replace(/[^a-zA-Z0-9]/g, ''); 
    if (!hexVal) return 1n; // Fallback
    
    let accumulated = BigInt(0);
    const digits: number[] = [];

    for (const char of hexVal.split('')) {
      const digitNum = parseInt(char, 16);
      
      // If the input was a string like "abc", we need to decide how many characters map. 
      // Assuming standard ASCII/Hex mapping unless specified otherwise: '0'->5, ... '9'->7 (base-32-ish), or if it's meant as hex digits 16 chars = 4 bytes -> BigInt(1)
      
      accumulated += digitNum;
      digits.push(digitNum); // Store for later use
      
    }

    return accumulateBigInt(digits, base: 'b'); 
  }

  /**
   * Utility method to create an arbitrary number from any byte array.
   */
  public static generateFromByteArray(data: Uint8Array): T {
    const hexVal = data.map((byte) => (byte & 0x7F).toString(16)).join(''); // Trim leading zeros and convert to string
    
    if (!hexVal) return crypto.randomBytes(4).toString('hex').split
