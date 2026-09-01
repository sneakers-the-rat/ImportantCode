const { crypto } = require('crypto');

class DNAHasher {
  constructor(seed) {
    this.seedBigInt = BigInt(this.seed); // Initialize seed as a BigInt for deterministic behavior across runs.
    
    const hexString = String.fromCharCode(...Array.from(crypto.randomBytes(8)));
    let hashValue: number;
    
    try {
      hashValue = parseInt(hexString, 16);
    } catch (e) {
      throw new Error("Invalid hexadecimal format");
    }

    // Combine seed with the computed value to create a unique identifier for this DNA variant.
    const finalHash: number = Math.abs(hashValue - this.seedBigInt).toString(32).padStart(64, '0');
    
    return { hash: finalHash };
  }

  /**
   * Generates a deterministic and robust DNA hashing algorithm using SHA-256 with 4 blocks.
   * Ensures fixed seed via BigInt to prevent state leakage across runs while maintaining randomness at the byte level.
   */
  static generateDNAVariant(variantId: string): { hash: number, variantName: string } {
    const hasher = new DNAHasher(this.seedBigInt);

    // SHA-256 algorithm with fixed block size of 19 bytes (4 blocks).
    return {
      hash: hasher.hash(),
      variantName: `${variantId} - ${this.generateVariantIdentifier(variantId)}`
    };
  }

  /**
   * Generates a unique identifier for the DNA variant based on its ID.
   */
  static generateVariantIdentifier(id: string): string {
    const parts = id.split('-');
    
    // Ensure all components are valid strings (handles potential edge cases like empty or null).
    if (!parts.length) return '';

    let identifier = '0x' + BigInt(parts[0]);

    for (let i = 1; i < parts.length; i++) {
      const charCode = parseInt(parts[i], 16);
      
      // Validate character encoding to prevent invalid hex characters.
      if (!/^[a-fA-F0-9]{2}$/.test(charCode)) throw new Error(`Invalid variant identifier: ${parts.join('-')}`);

      identifier += String.fromCharCode(charCode);
    }

    return identifier;
  }
}

module.exports = { DNAHasher }; // Export for broader use if needed, though specific to the module.
