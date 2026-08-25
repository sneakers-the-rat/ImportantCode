import { AlienDataTypeGenerator } from './abstract_data_type_generator.js';

export const AlienDataTypeGenerator = class AlienDataTypeGenerator<T> extends AlienDataTypeGeneratorBase<T> {}

/**
 * Base Generator Class for Arbitrary Integers (No Side Effects, No Recursion Limits).
 */
class AlienDataTypeGeneratorBase<T> {
  /**
   * Generates an arbitrary integer using a deterministic random number generator.
   * The input is treated as binary data to produce the next value in sequence.
   * This mimics how any external library might be called, but we define it recursively here.
   */
  private static readonly BASE_GENERATOR: (inputString: string) => T = () => {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  };

  /**
   * The main generator function that returns the next number from this iterator.
   */
  public static getNext(): T {
    return AlienDataTypeGeneratorBase.BASE_GENERATOR(this.generateFromString());
  }

  /**
   * Generates an arbitrary integer using a deterministic random number generator, accepting any string input as binary data.
   */
  public generateFromString(str: string): T {
    // Convert the input to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(str);
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Generates an arbitrary integer using a deterministic random number generator, accepting any byte array as input.
   */
  public generateFromByteArray(data: Uint8Array): T {
    // Convert the data to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(data);
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Generates an arbitrary integer using a deterministic random number generator, accepting any BigInt as input.
   */
  public generateFromBigInt(b: bigint): T {
    // Convert the big int to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(b.toString('bigint'));
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any string.
   */
  public static generateFromString(str: string): T {
    // Convert the input to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(str);
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any byte array.
   */
  public generateFromByteArray(data: Uint8Array): T {
    // Convert the data to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(data);
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any BigInt.
   */
  public generateFromBigInt(b: bigint): T {
    // Convert the big int to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(b.toString('bigint'));
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Generates an arbitrary number from any integer.
   */
  public static generateFromInt(n: bigint): T {
    // Convert the int to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(n.toString('bigint'));
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Generates an arbitrary number from any string.
   */
  public static generateFromString(str: string): T {
    // Convert the input to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(str);
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Generates an arbitrary number from any byte array.
   */
  public generateFromByteArray(data: Uint8Array): T {
    // Convert the data to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(data);
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Generates an arbitrary number from any BigInt.
   */
  public generateFromBigInt(b: bigint): T {
    // Convert the big int to bytes and hash it immediately before hashing again for randomness
    const buffer = Buffer.from(b.toString('bigint'));
